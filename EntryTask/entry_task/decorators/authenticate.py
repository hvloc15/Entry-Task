
from entry_task.response_model import ResponseBody
from django.http import HttpResponseBadRequest
from entry_task.models.user import User
from entry_task.exceptions import AuthenticationFailed
from entry_task import settings
import jwt
import json

jwt_decode_handler = settings.JWT_DECODE_HANDLER


def get_request_authorization_header(request):
    try:
        auth_header = request.META['HTTP_AUTHORIZATION']
        return auth_header
    except KeyError:
        raise KeyError("No authorization header")


def validate_authorization_header(header):
    try:
        auth = header.split()
        auth_header_prefix = settings.JWT_AUTH_HEADER_PREFIX.lower()
        if not auth or auth[0].lower() != auth_header_prefix or len(auth)!=2:
            raise AuthenticationFailed("Invalid authorization header")
    except Exception as e:
        raise AuthenticationFailed(e.message)


def get_payload(token):
    try:
        payload = jwt_decode_handler(token)
    except jwt.ExpiredSignature:
        raise AuthenticationFailed("Token expired")
    except jwt.DecodeError:
        raise AuthenticationFailed("Wrong token")
    return payload


def authenticate_auth_header(auth_header):
    validate_authorization_header(auth_header)
    payload = get_payload(auth_header.split()[1])
    user = User.authenticate_payload(payload)
    return user


def authenticate_required(view_func):
    def _view(request,*args, **kwargs):
        try:
            auth_header = get_request_authorization_header(request)
            user = authenticate_auth_header(auth_header)
            return view_func(request,int(user.user_id), *args, **kwargs)
        except Exception as e:
            response_body = ResponseBody(False, e.message).as_json()
            return HttpResponseBadRequest(json.dumps(response_body), content_type="application/json")

    _view.__name__ = view_func.__name__
    _view.__dict__ = view_func.__dict__
    _view.__doc__ = view_func.__doc__
    return _view


