from django.urls import path
from . import views

app_name = "register"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    # path('edit/', views.edit.as_view(), name='edit'),
    path('logout/', views.logout, name='logout')
]