from django.urls import path
from . import views


urlpatterns = [
    path('', views.strings, name='strings'),
    path('strings/<slug:slug>', views.strings_detail, name='strings_details'),
]
