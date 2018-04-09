from django.views import generic


# Checkout news.views were the home page is defined and rendered from there

# class HomePage(generic.TemplateView):           # this home is removed and added to news app
#     template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
