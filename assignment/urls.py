from django.conf.urls import url
from assignment import views


# I Edited
app_name = "assignment"
# end I edited

# I Made
urlpatterns = [
    url(r'^assignment/$', views.AssignmentListView.as_view(), name='assignment_list'),
    url(r'^assignment/(?P<course_val>\w+)$', views.assignment_list_by_course, name='assignment_list_by_course'),

    url(r'^slide/$', views.SlideListView.as_view(), name='slide_list'),
    url(r'^slide/(?P<course_val>\w+)$', views.slide_list_by_course, name='slide_list_by_course'),

    url(r'^assignment/new/$', views.AssignmentCreateView.as_view(), name='assignment_new'),
    url(r'^slide/new/$', views.SlideCreateView.as_view(), name='slide_new'),

    url(r'^assignment/(?P<pk>\d+)/remove/$', views.AssignmentDeleteView.as_view(), name='assignment_remove'),
    url(r'^slide/(?P<pk>\d+)/remove/$', views.SlideDeleteView.as_view(), name='slide_remove'),

    url(r'^assignment/(?P<pk>\d+)/update/$', views.AssignmentUpdateView.as_view(), name='assignment_update'),
    url(r'^slide/(?P<pk>\d+)/update/$', views.SlideUpdateView.as_view(), name='slide_update'),




    # url(r'^question/(?P<pk>\d+)/edit/$', views.QuestionUpdateView.as_view(), name='question_edit'),
    # url(r'^question/(?P<pk>\d+)$', views.AssignmentDetailView.as_view(), name='question_detail'),
    # Comments :
    # url(r'^question/(?P<pk>\d+)/comment/$', views.add_comment_to_question, name='add_comment_to_question'),
    # url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]