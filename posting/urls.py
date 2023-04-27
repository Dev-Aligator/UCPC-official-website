from django.urls import path
from . import views

app_name = "posting"
urlpatterns = [
    path('posts/', views.post, name='posts'),
]