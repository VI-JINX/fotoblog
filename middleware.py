from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class AdminOnlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return HttpResponseForbidden('Vous n\'êtes pas autorisés à consulter l\'espace administrateur')
        return self.get_response(request)