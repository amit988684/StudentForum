from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import forumapp.urls    # My Import
import profiles.urls
import accounts.urls
import assignment.urls
from . import views

# Check out news app for the definiton
from news.views import NewsListView

urlpatterns = [
    # Added for the news content at the home page
    url(r'^$', NewsListView.as_view(), name='home'),


    # url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),

    # My App
    url(r'forumapp/', include(forumapp.urls, namespace='forumapp')),
    url(r'sharing/', include(assignment.urls, namespace='assignment')),

   # Google Auth
    url(r'^auth/', include('social_django.urls', namespace='social')),

    # Contact Us
    url(r'^contact/', include('contactus.urls', namespace='contactus')),
    url(r'^event/', include('event.urls', namespace='event')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
