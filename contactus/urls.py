from django.conf.urls import include, url
from .views import ContactUsView

app_name = 'contactus'

urlpatterns = [
    url(r'^$', ContactUsView.as_view(), name='contactus_view'),
]