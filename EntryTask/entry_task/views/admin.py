# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from entry_task.helpers import response_helpers
from django.http import HttpResponseRedirect
from entry_task.forms import LoginForm, UploadEventInfoForm, UploadImagesForm
from django.views.decorators.cache import never_cache
from entry_task.models import Session, Image, EventInfo
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse


# /admin/login
# Create your views here.
@never_cache
@csrf_protect
def login(request):
    session_id = request.COOKIES.get('session_id')
    next_page = reverse('admin_page')
    if session_id is None:
        login_success = True
        if request.method == 'POST':
            form = LoginForm(request.POST)
            login_success = form.validate_credentials()
            if login_success:
                session_id = Session.objects.create_session(form.get_username())
                response = redirect(next_page)
                response_helpers.set_cookie(response,"session_id",session_id)
                return response
        form = LoginForm()
        context = {
            'form': form,
            'login_success': login_success,
        }
        return render(request, 'login/login.html', context)
    return redirect(next_page)

# /admin
@never_cache
@csrf_protect
def admin_page(request):
    sid = request.COOKIES.get('session_id')
    if sid is None:
        return redirect(reverse('admin_login_page'))
    if request.method == 'POST':
        event_info_form = UploadEventInfoForm(request.POST)
        images_info_form = UploadImagesForm(request.POST, request.FILES)
        if event_info_form.is_valid() and images_info_form.is_valid():
            form_input = event_info_form.get_event_info_values()
            event_info = EventInfo.create(**form_input)
            event_info.save()
            images = images_info_form.get_list_images()
            for image in images:
                photo = Image(event_id= event_info.event_id, src=image)
                photo.save()
            return HttpResponseRedirect(reverse('admin_page'))
    else:
        event_info_form = UploadEventInfoForm()
        images_info_form = UploadImagesForm()
    context = {
        "event_form": event_info_form,
        "images_form": images_info_form,
    }
    return render(request,"admin/admin.html",context)

# /admin/logout
@never_cache
@csrf_protect
def logout(request):
    session_id = request.COOKIES.get('session_id')
    if session_id is not None:
        session_id = str(session_id)
        response = render(request,"logout/logout.html")
        response_helpers.invalidate_cookie(response,"session_id")
        Session.objects.delete_session(session_id)
        return response
    else:
        return redirect(reverse("admin_login_page"))