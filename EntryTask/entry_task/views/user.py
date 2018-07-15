# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from entry_task.services import user_services
import json
from entry_task.decorators.authenticate import authenticate_required
from entry_task.helpers import request_helpers, response_helpers
from entry_task.response_model import ResponseBody
from django.views.decorators.http import require_http_methods


# /users/login
@require_http_methods(["POST"])
def login(request):
    token = user_services.login(*request_helpers.get_user_credentials_from_request(request))
    response_body = ResponseBody(True, "Login successfully").as_json()
    response = HttpResponse(json.dumps(response_body), content_type="application/json")
    response_helpers.set_header_login_response(response,token)
    return response

# /users
@require_http_methods(["GET"])
@authenticate_required
# Create your views here.
def get_list_users(request,current_user_id):
    data = user_services.get_list_user()
    return HttpResponse(json.dumps(data), content_type="application/json")

# /users/id
@require_http_methods(["GET"])
@authenticate_required
def get_user(request, current_user_id, user_id):
    data = user_services.get_user_by_id(user_id)
    return HttpResponse(json.dumps(data), content_type="application/json")

# /users/id/activities
@require_http_methods(["GET"])
@authenticate_required
def get_activities(request, current_user_id, user_id):
    data = user_services.get_activities(user_id)
    return HttpResponse(json.dumps(data), content_type="application/json")



