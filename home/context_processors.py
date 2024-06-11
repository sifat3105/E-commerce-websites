from django.urls import reverse
from auth_app.models import profile  # Adjust the import if necessary

def account_context(request):
    first_name = None
    log_reg = 'Log In / Sign Up'
    log_reg_link = reverse('login_registration')
    
    if request.user.is_authenticated:
        first_name = request.user.first_name
        log_reg = request.user.username
        log_reg_link = reverse('account')
    
    return {
        'first_name': first_name,
        'log_reg': log_reg,
        'log_reg_link': log_reg_link,
        'Profile': profile.objects.all()
    }