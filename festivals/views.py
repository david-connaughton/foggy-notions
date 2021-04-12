from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import Festival

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

import os

if os.path.exists("env.py"):
    import env

# MailChimp Settings
api_key = os.environ.get('MAILCHIMP_API_KEY')
server = os.environ.get('MAILCHIMP_DATA_CENTER')
list_id = os.environ.get('MAILCHIMP_EMAIL_LIST_ID')


def subscribe(email):
    """
    Contains code handling the communication to the mailchimp api
    to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


def festivals(request):
    """ A view to render concerts"""
    festivals = Festival.objects.filter(publish__lte=timezone.now())
    template = 'festivals/festivals.html'
    context = {
        'festivals': festivals,
    }
    if request.method == 'POST':
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Thank you for subscribing!")  # message
        festivals = Festival.objects.filter(publish__lte=timezone.now())
        template = 'festivals/festivals.html'
        context = {
            'festivals': festivals,
        }
        return render(request, "festivals/festivals.html", context)
    return render(request, template, context)


def festival_detail(request, slug):
    """A custom view for individual concert details"""
    festival = get_object_or_404(Festival, slug=slug)
    template = 'festivals/festival_details.html'
    context = {
        'festival': festival,
    }
    if request.method == 'POST':
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Thank you for subscribing!")  # message
        concert = get_object_or_404(Concert, slug=slug)
        template = 'festivals/festival_details.html'
        context = {
            'festivals': festivals,
        }
        return render(request, 'festivals/festival_details.html', context)
    return render(request, 'festivals/festival_details.html', context)
