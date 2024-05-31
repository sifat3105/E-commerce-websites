from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        auth_prohibited_paths = [
            reverse('login_registration'),
        ]

        auth_required_paths = [
            reverse('home'),
        ]

        if request.user.is_authenticated and request.path in auth_prohibited_paths:
            return redirect('home')
        
        if not request.user.is_authenticated and request.path in auth_required_paths:
            return redirect('login_registration')

        response = self.get_response(request)
        return response
