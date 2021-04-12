from django.urls import path
from . import views


urlpatterns = [
    path('', views.festivals, name='festivals'),
    path('festival/<slug:slug>', views.festival_detail, name='festival_details'),
]
