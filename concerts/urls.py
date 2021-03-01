from django.urls import path
from . import views
from .views import ConcertListView


urlpatterns = [
    path('', ConcertListView.as_view(), name='concerts'),
]
