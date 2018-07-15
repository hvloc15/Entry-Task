from entry_task.helpers import datetime_helpers
from entry_task.exceptions import WrongInputType
import json, os


def get_from_body_request(request):
    try:
        body = json.loads(request.body)
        date = datetime_helpers.string_to_timestamp(body["date"])
        content = body.get("content","")
        return date, content
    except:
        raise WrongInputType("Wrong input type")


def get_query_strings(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    if page <= 0 or page_size < 0:
        raise WrongInputType("Invalid values of query string parameters")
    event_type = request.GET.get("type", "none")
    start_date = request.GET.get("start_date", 0)
    end_date = request.GET.get("end_date", 0)
    return page, page_size, event_type, start_date, end_date


def get_user_credentials_from_request(request):
    try:
        body = json.loads(request.body)
        return body["username"], body["password"]
    except:
        raise WrongInputType("Wrong input type")


def get_basename(request):
    path = request.path
    return os.path.basename(path)