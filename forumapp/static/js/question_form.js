/**
 * Created by robhood97 on 3/22/18.
 */
var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

// Best viewed in Chrome
// Click anywhere to make your own lightning!

//=============================
// Consts
//=============================
var HAS_FLASH = true;
var TIME_BETWEEN_LIGHTNING = 1000;

var MAX_POINTS = 120;
var MAX_X_DISTANCE = 9; // 10 - 30
var MAX_Y_DISTANCE = 8; // 10 - 30
var MAX_WIDTH = 3; // 1 - 10

var FADE_INCREMENT = 0.013; // 0 - 0.02

var LIGHTNING_CHANCE = 0.03;
var SHEET_CHANCE = 0.2;
var BRANCH_CHANCE = 0.01;
var FLICKER_CHANCE = 0.023;
var BRANCH_BRANCH_CHANCE = 0.90;

//=============================
// Helpers
//=============================
var getTimestamp = function getTimestamp() {
  return new Date().getTime();
};

var random = function random() {
  var max = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 1;
  var unsigned = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : false;

  return unsigned ? (Math.random() - 0.5) * 2 * max : Math.random() * max;
};

//=============================
// Main
//=============================
var lightningCanvas = document.getElementById('lightning');
var ctx = lightningCanvas.getContext('2d');
var cloudLightningCanvas = document.getElementById('cloudlightning');
var clCtx = cloudLightningCanvas.getContext('2d');
var lightningSheetCanvas = document.getElementById('lightningSheet');
var lsCtx = lightningSheetCanvas.getContext('2d');

var HAS_CLOUD_EFFECTS = true;

var lightning = [];
var cloudLightning = [];
var flashes = [];
var lightningSheets = [];

var stageWidth = 0;
var stageHeight = 0;
var previousTimestamp = getTimestamp();
var previousRender = getTimestamp();

var loop = function loop() {
  ctx.clearRect(0, 0, stageWidth, stageHeight);
  clCtx.clearRect(0, 0, stageWidth, stageHeight);
  lsCtx.clearRect(0, 0, stageWidth, stageHeight);

  lightning.forEach(function (path) {
    path.animate();
    path.render();
  });

  if (HAS_CLOUD_EFFECTS) {
    cloudLightning.forEach(function (cloud) {
      cloud.animate();
      cloud.render();
    });

    lightningSheets.forEach(function (lightningSheet) {
      lightningSheet.animate();
      lightningSheet.render();
    });
  } else {
    cloudLightning.forEach(function (cloud) {
      return cloud.alpha = 0;
    });
    lightningSheets.forEach(function (cloud) {
      return cloud.alpha = 0;
    });
  }

  if (HAS_FLASH) {
    flashes.forEach(function (path) {
      path.animate();
      path.render();
    });
  }

  // create lightning or lightning sheet
  if (random() < LIGHTNING_CHANCE && getTimestamp() - previousTimestamp > TIME_BETWEEN_LIGHTNING) {

    if (random() > 0.4) {
      lightning.push(new Lightning());
    } else {
      lightningSheets.push(new LightningSheet());
    }

    previousTimestamp = getTimestamp();
  }

  lightning = lightning.filter(function (path) {
    return path.alpha > 0;
  });
  cloudLightning = cloudLightning.filter(function (cloud) {
    return cloud.alpha > 0;
  });
  flashes = flashes.filter(function (sheet) {
    return sheet.alpha > 0;
  });
  lightningSheets = lightningSheets.filter(function (sheet) {
    return sheet.alpha > 0;
  });

  requestAnimationFrame(loop);
};

var Lightning = function () {
  function Lightning(ox, oy, width) {
    var isBranch = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : false;
    var branchDirection = arguments[4];

    _classCallCheck(this, Lightning);

    var x = ox || random(stageWidth);
    var y = oy || 40 + random(100);
    var newCloud = void 0;

    this.paths = [];
    this.red = 255;
    this.green = 255;
    this.blue = 255;
    this.alpha = 1;
    this.hasEnded = false;
    this.width = width || random(MAX_WIDTH) + 1;
    this.isBranch = isBranch;
    this.xDeviation = isBranch ? 1.3 : 1;
    this.branchDirection = branchDirection || (Math.random() - 0.5) * 2;
    this.flickerCount = 0;
    this.clouds = [];

    this.paths.push({
      x: x,
      y: y
    });

    if (HAS_FLASH) {
      flashes.push(new Flash(this.width));
    }

    if (!this.isBranch) {
      newCloud = new CloudLightning(x, y, this.width);
      cloudLightning.push(newCloud);
      this.clouds.push(newCloud);
    }

    if (this.isBranch) {
      this.width = 1;
    }
  }

  _createClass(Lightning, [{
    key: 'animate',
    value: function animate() {
      var newLines = 3 + random(5);
      var branchChance = this.isBranch ? BRANCH_BRANCH_CHANCE : BRANCH_CHANCE;

      if (!this.hasEnded) {
        var previousPoint = this.getLastPoint();
        var lastX = previousPoint.x;
        var lastY = previousPoint.y;
        var newX = void 0,
            newY = void 0;
        var xDirection = void 0;

        // add new extensions
        for (var i = 0; i < newLines; i++) {
          xDirection = this.isBranch ? this.branchDirection : (Math.random() - 0.5) * 2;
          newX = lastX + xDirection * MAX_X_DISTANCE * this.xDeviation;
          newY = lastY + random(MAX_Y_DISTANCE) + 2;

          lastX = newX;
          lastY = newY;
          this.paths.push({
            x: newX,
            y: newY
          });

          if (this.isBranch && random() < 0.03) {
            lightning.push(new Lightning(lastX, lastY, this.width, true));
          }
        }

        // when to stop extending
        this.hasEnded = lastY / stageHeight > 0.8 || random() > 0.6 && this.paths.length > MAX_POINTS * 3 / 4 || this.paths.length > MAX_POINTS || this.isBranch && this.paths.length > 5;

        // create branches
        if (random() > branchChance && this.paths.length > 5 && this.paths.length < MAX_POINTS * 2 / 3) {
          lightning.push(new Lightning(lastX, lastY, this.width, true));
        }
      }

      // fade out
      if (this.alpha > 0) {
        this.alpha -= FADE_INCREMENT;

        // fade out purple
        if (this.alpha < 0.5) {
          this.green -= 4.5;
        }

        if (this.isBranch) {
          this.alpha -= FADE_INCREMENT / 2;
        }
      }

      // cool flicker
      if (!this.isBranch && random() < FLICKER_CHANCE && this.flickerCount < 2 && this.alpha > 0.3) {
        this.alpha = 1;
        this.green = 240;
        this.flickerCount++;

        this.clouds.map(function (cloud) {
          cloud.alpha = random(0.6) + 0.3;
        });
      }

      if (this.isBranch && this.flickerCount > 0 || this.alpha < 0) {
        this.alpha = 0;
      }
    }
  }, {
    key: 'render',
    value: function render() {
      var colour = this.getColour();

      ctx.beginPath();
      ctx.strokeStyle = colour;
      ctx.lineWidth = this.width;

      //if (this.flickerCount === 0) {
      //  ctx.shadowBlur = this.width * 3;
      //  ctx.shadowColor = colour;
      //}

      this.paths.forEach(function (path) {
        ctx.lineTo(path.x, path.y);
      });

      ctx.stroke();
    }
  }, {
    key: 'getColour',
    value: function getColour(red, green, blue, alpha) {
      return 'rgba(' + (red || this.red) + ', ' + (green || this.green) + ', ' + (blue || this.blue) + ', ' + (alpha || this.alpha) + ')';
    }
  }, {
    key: 'getLastPoint',
    value: function getLastPoint() {
      if (this.paths.length > 0) {
        var lastPoint = this.paths[this.paths.length - 1];

        return {
          x: lastPoint.x,
          y: lastPoint.y
        };
      } else {
        return { x: 0, y: 0 };
      }
    }
  }]);

  return Lightning;
}();

var Flash = function () {
  function Flash() {
    var flash = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 1;

    _classCallCheck(this, Flash);

    this.alpha = 0.09 * flash;
  }

  _createClass(Flash, [{
    key: 'animate',
    value: function animate() {
      this.alpha -= FADE_INCREMENT * 2;
    }
  }, {
    key: 'render',
    value: function render() {
      ctx.beginPath();
      ctx.fillStyle = 'rgba(50, 48, 51, ' + this.alpha + ')';
      ctx.fillRect(0, 0, stageWidth, stageHeight);
    }
  }]);

  return Flash;
}();

var LightningSheet = function () {
  function LightningSheet(x, y) {
    var isRoot = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : true;

    _classCallCheck(this, LightningSheet);

    this.alpha = random(0.6) + 0.2;
    this.x = x || random(stageWidth);
    this.y = y || random(stageHeight * 0.6) - 100;
    this.size = random(50) + 40;

    // size proportionately to the horizon to create perspective
    this.size = (1 - this.y / stageHeight * 0.6) * this.size;

    if (isRoot) {
      var sheetX = void 0,
          sheetY = void 0;

      for (var i = 0; i < random(12) + 4; i++) {
        sheetX = this.x + random(300, true);
        sheetY = this.y + random(80, true);
        lightningSheets.push(new LightningSheet(sheetX, sheetY, false));
      }
    }
  }

  _createClass(LightningSheet, [{
    key: 'animate',
    value: function animate() {
      this.alpha -= FADE_INCREMENT * 0.8;

      if (this.alpha < 0.3 && random() < 0.025) {
        this.alpha += random(0.4);
      }
    }
  }, {
    key: 'render',
    value: function render() {
      lsCtx.save();

      lsCtx.scale(2, 1);

      lsCtx.beginPath();
      lsCtx.arc(this.x / 2, this.y, this.size, 2 * Math.PI, false);
      lsCtx.closePath();
      lsCtx.restore();

      lsCtx.filter = 'blur(' + this.size + 'px)';
      lsCtx.fillStyle = 'rgba(100, 100, 100, ' + this.alpha + ')';
      lsCtx.fill();
      lsCtx.shadowColor = '#999999';
      lsCtx.shadowBlur = this.size;
    }
  }]);

  return LightningSheet;
}();

var CloudLightning = function () {
  function CloudLightning(x, y, size) {
    _classCallCheck(this, CloudLightning);

    this.x = x;
    this.y = y;
    this.size = size * 3 * random(2) + 10;
    this.alpha = 1;
  }

  _createClass(CloudLightning, [{
    key: 'animate',
    value: function animate() {
      this.alpha -= FADE_INCREMENT;
    }
  }, {
    key: 'render',
    value: function render() {
      clCtx.save();

      clCtx.scale(2.5, 1);

      clCtx.beginPath();
      clCtx.arc(this.x / 2.5, this.y, this.size, 2 * Math.PI, false);
      clCtx.restore();

      clCtx.filter = 'blur(' + this.size + 'px)';
      clCtx.fillStyle = 'rgba(255, 255, 255, ' + this.alpha + ')';
      clCtx.fill();
      clCtx.shadowColor = '#eeeeff';
      clCtx.shadowBlur = this.size * 8 + 50;
    }
  }]);

  return CloudLightning;
}();

//=============================
// Setup
//=============================

var updateCanvasSize = function updateCanvasSize() {
  stageWidth = window.innerWidth;
  stageHeight = window.innerHeight;

  lightningCanvas.width = stageWidth;
  lightningCanvas.height = stageHeight;

  cloudLightningCanvas.width = stageWidth;
  cloudLightningCanvas.height = stageHeight;

  lightningSheetCanvas.width = stageWidth;
  lightningSheetCanvas.height = stageHeight * 0.8;
};

$(window).on('mousedown', function (e) {
  lightning.push(new Lightning(e.clientX, e.clientY));
});

updateCanvasSize();
$(window).resize(updateCanvasSize);

// create forest
var $tree = $('.tree');
for (var i = 0; i < 150; i++) {
  $tree.clone().appendTo('body').css({
    top: random(40) + 30 + '%',
    left: random(stageWidth * 0.7, true),
    transform: 'scale(' + (random(0.5) + 0.5) + ') scaleX(' + (random() > 0.5 ? -1 : 1) + ')',
    display: 'inline'
  });
}

// watch toggle
$('#cloudInput').on('click', function () {
  HAS_CLOUD_EFFECTS = $(this).is(':checked');
});

setTimeout(function () {
  $('.toggles').fadeIn();
}, 6000);

//=============================
// Run it!
//=============================

lightning.push(new Lightning(400, 100));
loop();