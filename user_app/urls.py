from django.urls import path
from user_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),  # user register url

    path('login/', views.login_user, name='login'),  # user login url

    path('logout/', views.logout_user, name='logout'),  # user logout url

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),  # user password reset url
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),  # user password reset done message url
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),  # user password change url
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),  # user password change complete message url
         name='password_reset_complete'),

    path('verify/<str:token>/<int:id>/', views.verify_view, name='verify_view'),  # token generators url

    path('change_password/', views.change_password, name='change_password'),  # password change url

    path('settings/<int:id>/', views.settings_user, name='settings'),  # user settings url

]
