from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm,PasswordResetConfirmViewForm,passwordchangingform

urlpatterns = [     
    path('login/', views.login_1, name='auth_login'),
    path('logout/', views.logout_1, name='auth_logout'),
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset.html',form_class=UserPasswordResetForm),name = "reset_password"),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password-reset-sent.html'),name ="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password-reset-confirm.html',form_class=PasswordResetConfirmViewForm),name = "password_reset_confirm"),
    path('reset-password/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password-complete.html'),name = "password_reset_complete"),
    path('change_password/',views.change_password, name='change_password'),
    path('Dashboard/', views.home, name='home'),
]