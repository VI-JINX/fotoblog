from django.urls import path, reverse_lazy
from . views import *
from django.contrib.auth.views import *


urlpatterns = [
    path('', LoginView.as_view(template_name = 'authentication/login_page.html', redirect_authenticated_user=True), name = 'login'),
    path('logout/', LogoutView.as_view(next_page ='login'), name = 'logout'),
    path('change_password/', PasswordChangeView.as_view(template_name = 'authentication/password_change.html', success_url = reverse_lazy('change_password_done')), name = 'change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(template_name = 'authentication/password_change_done.html'), name = 'change_password_done' ),
    path('inscription/', sign_up.as_view(), name = 'sign_up'),
    path('reset_password/',passwordresetview.as_view(), name = 'password_reset' ),
    path('reset_password_confirm/', passwordchangedoneview.as_view(), name = 'password_reset_confirm'),
    path('reset_password_confirm_done/<uidb64>/<token>/', passwordresetdoneview.as_view(), name = 'password_reset_confirm_done'),
    path('verified_your_account/', complete_verification, name = 'complete_verification'),
    path('active/account/<uidb64>/<token>/', active_account, name = 'active_account')
    
]
