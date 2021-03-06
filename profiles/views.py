from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from django.shortcuts import render
from django.views.generic import ListView

# My Added
from django.contrib.auth.decorators import login_required
from .models import Profile

class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        profile_form.save_m2m()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")

# My Added


def all_user_view(request):
    return render(request,'all_user_view.html')


class UserListView(LoginRequiredMixin,ListView):
    template_name = 'all_user_view_final.html'

    def get_queryset(self):
        return Profile.objects.all()

    # def all_users(request):
    #     context = {'users_list1': Profile.objects.all()}
    #     return render(request,'all_user_view_final.html',context=context)

#
# @login_required
# def user_list_by_privilage(request,**kwargs):
#     # print (kwargs)
#     user_type = str(kwargs['user_type'])
#     profile_list = Profile.objects.filter()
#     # courses = Course.objects.all()
#     # print("amit" + query)
#     return render(request,'all_user_view_final.html',{'profile_list': profile_list})
