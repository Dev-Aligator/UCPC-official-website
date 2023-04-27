from django.urls import path
from . import views

app_name = "register"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('profile/create/', views.create_profile.as_view(), name='create'),
    path('profile/view/', views.view_profile.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile.as_view(), name='edit'),
    path('logout/', views.logout, name='logout')
]