from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views 


app_name = "register"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('profile/create/', views.create_profile.as_view(), name='create'),
    path('profile/view/', views.view_profile.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile.as_view(), name='edit'),
    path('logout/', views.logout, name='logout'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_confirm.html", success_url = reverse_lazy('register:login')), name='password_reset_confirm'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]