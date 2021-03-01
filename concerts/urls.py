from django.urls import path
from . import views


urlpatterns = [
    path('', views.concerts, name='concerts'),
    path('concert/<slug:slug>', views.concert_detail, name='concert_details'),
]
