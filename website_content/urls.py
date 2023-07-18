from django.urls import path, re_path
from .views import home_view, course_detail, filtered_content, plan_details
from . import views


app_name = 'website_content'
urlpatterns = [
    path('home/', home_view, name='home'),
    path('home/<str:name>/', course_detail, name='course_detail'),
    path('home/<str:name>/<str:slug>/', filtered_content, name='filtered_content'),
    path('plan/', plan_details, name='plan_details'),
]
