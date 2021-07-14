from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import String

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


def strings(request):
    """ A view to render concerts"""
    strings = String.objects.filter(publish__lte=timezone.now())
    template = 'strings/strings.html'
    context = {
        'strings': strings,
    }
    if request.method == 'POST':
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Thank you for subscribing!")  # message
        strings = String.objects.filter(publish__lte=timezone.now())
        template = 'strings/strings.html'
        context = {
            'strings': strings,
        }
        return render(request, "strings/strings.html", context)
    return render(request, template, context)
