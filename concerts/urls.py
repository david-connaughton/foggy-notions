from django.urls import path
from . import views
from .views import ConcertListView, ConcertDetailView


urlpatterns = [
    path('', ConcertListView.as_view(), name='concerts'),
    path('concert/<slug:slug>', ConcertDetailView.as_view(), name='concert_details'),
]
