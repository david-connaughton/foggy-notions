from django.shortcuts import render, get_list_or_404
from django.utils import timezone

from django.views.generic import (
    ListView,
)

from .models import Concert


class ConcertListView(ListView):
    model = Concert
    template_name = 'concerts/concerts.html'
    context_object_name = 'concerts'

    def get_queryset(self):
        return Concert.objects.filter(publish__lte=timezone.now())
