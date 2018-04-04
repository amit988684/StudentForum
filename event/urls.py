from django.conf.urls import url
from . import views


# I Edited
app_name = "event"
# end I edited

# I Made

urlpatterns = [
    url(r'^new/$', views.EventCreateView.as_view(), name='event_new'),
    url(r'^list/$', views.EventListView.as_view(), name='event_list'),
    url(r'^remove/(?P<pk>\d+)/$', views.EventDeleteView.as_view(), name='event_remove'),
    url(r'^update/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='event_update'),
    # url(r'^assignment/(?P<course_val>\w+)$', views.assignment_list_by_course, name='assignment_list_by_course'),
]