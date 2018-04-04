from django.conf.urls import url
from . import views


# I Edited
app_name = "event"
# end I edited

# I Made

urlpatterns = [
    url(r'^new/$', views.EventCreateView.as_view(), name='event_new'),
    # url(r'^assignment/(?P<course_val>\w+)$', views.assignment_list_by_course, name='assignment_list_by_course'),
]