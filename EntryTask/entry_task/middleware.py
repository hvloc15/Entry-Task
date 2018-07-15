from entry_task.response_model import ResponseBody
from django.http import HttpResponse
import json


class ExceptionHandlerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self,request, exception):
        response_body = ResponseBody(False, exception.message).as_json()
        status_code = 500
        if hasattr(exception, 'status_code'):
            status_code = exception.status_code
        response = HttpResponse(json.dumps(response_body), status=status_code, content_type="application/json")
        return response
