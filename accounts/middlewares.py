from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile
 
LOGIN_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_URLS'):
    LOGIN_URLS += [compile(expr) for expr in settings.LOGIN_URLS]

LOGIN_REQUIRED_URLS=[]
if hasattr(settings, 'LOGIN_REQUIRED_URLS'):
    LOGIN_REQUIRED_URLS += [compile(expr) for expr in settings.LOGIN_REQUIRED_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        next = '?next=/'+path
        # To Prevent Unauthenticated Users to access the URLS
        if not request.user.is_authenticated:
            if any(m.match(path) for m in LOGIN_REQUIRED_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL+next)

        if request.user.is_authenticated:
            if any(m.match(path) for m in LOGIN_URLS):
                return HttpResponseRedirect('/')

        response = self.get_response(request)
        return response 
