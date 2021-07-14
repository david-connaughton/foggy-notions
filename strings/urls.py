from django.urls import path
from . import views


urlpatterns = [
    path('', views.strings, name='strings'),
    path('string/<slug:slug>', views.string_detail, name='string_details'),
]
