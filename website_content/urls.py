from django.urls import path, re_path
from . import views

app_name = 'website_content'
urlpatterns = [
    path('home/', views.home_view, name='home'),
]