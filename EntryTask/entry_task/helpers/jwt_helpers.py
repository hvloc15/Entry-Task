from __future__ import unicode_literals
from datetime import datetime
import importlib

import jwt


def jwt_payload_handler(user):
    from entry_task import settings

    return {
        'user_id': user.pk,
        'username': user.username,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }


def jwt_get_user_id_from_payload_handler(payload):
    user_id = payload.get('user_id')
    return user_id


def jwt_encode_handler(payload):
    from entry_task import settings
    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM
    ).decode('utf-8')


def jwt_decode_handler(token):
    from entry_task import settings
    options = {
        'verify_exp': settings.JWT_VERIFY_EXPIRATION,
    }

    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        settings.JWT_VERIFY,
        options=options,
        leeway=settings.JWT_LEEWAY
    )


def import_from_string(val):
    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for setting. %s: %s." % (val, e.__class__.__name__, e)
        raise ImportError(msg)





