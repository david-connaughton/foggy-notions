from django.shortcuts import render

# Create your views here.


def concerts(request):
    return render(request, 'concerts/concerts.html')
