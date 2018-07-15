import datetime
from django.conf import settings


def set_cookie(response, key, value, days_expire=7):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)


def invalidate_cookie(response, key):
    response.set_cookie(key, expires=0)


def set_no_cache(response):
    response['Cache-Control'] = "no-store"
    response['Pragma'] = "no-cache"


def set_header_login_response(response, token):
    response['Authorization'] = token
    set_no_cache(response)
