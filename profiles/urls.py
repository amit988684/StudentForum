from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),

#     My Added
    url(r'^all/users$', views.all_user_view, name='all_user'),
    url(r'^all/users/tab/$', views.UserListView.as_view(), name='all_user_tab'),
]
