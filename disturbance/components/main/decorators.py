import time
import traceback

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from rest_framework import serializers
# from rest_framework.request import Request
# from rest_framework.request import Request
from rest_framework.request import Request


def basic_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            from disturbance.components.main.utils import handle_validation_error
            handle_validation_error(e)
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))
    return wrapper


def update_settings_handler(func):
    """
    This function updates the settings values according to the subdomain
    @param func:
    @return:
    """
    def wrapper(*args, **kwargs):
        for param in args:
            if isinstance(param, HttpRequest) or isinstance(param, Request) or isinstance(param, WSGIRequest):
                web_url = param.META.get('HTTP_HOST', None)
                if web_url in settings.APIARY_URL:
                    settings.SYSTEM_NAME = settings.APIARY_SYSTEM_NAME
                    settings.SYSTEM_NAME_SHORT = 'Apiary'
                    settings.BASE_EMAIL_TEXT = 'disturbance/emails/apiary_base_email.txt'
                    settings.BASE_EMAIL_HTML = 'disturbance/emails/apiary_base_email.html'
        return func(*args, **kwargs)
    return wrapper


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed