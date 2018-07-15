# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from entry_task.decorators.authenticate import authenticate_required
from entry_task.helpers import request_helpers
from entry_task.services import event_services
from entry_task.response_model import ResponseBody
import json


# /events/id
@require_http_methods(["GET"])
@authenticate_required
def get_event(request, current_user_id, event_id):
    event = event_services.get_event(event_id)
    return HttpResponse(json.dumps(event),content_type="application/json")

# /events
@require_http_methods(["GET"])
@authenticate_required
def get_list_events(request, current_user_id):
    page, page_size, event_type, start_date, end_date = request_helpers.get_query_strings(request)
    list_events = event_services.get_list_events(page, page_size,event_type,start_date,end_date)
    return HttpResponse(json.dumps(list_events),content_type="application/json")

# /events/id/likes or /events/id/comments or /events/id/participates
@require_http_methods(['POST'])
@authenticate_required
def handle_activity(request, current_user_id, event_id):
    date, content = request_helpers.get_from_body_request(request)
    activity_type = request_helpers.get_basename(request)
    event_services.insert_activity(event_id, current_user_id, activity_type, date, content)
    response_body = ResponseBody(True, "Insert sucessfully").as_json()
    return HttpResponse(json.dumps(response_body), content_type="application/json")
