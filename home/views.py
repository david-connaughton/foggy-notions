from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages

from .models import Post

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


def home(request):
    posts = Post.objects.filter(
        publish__lte=timezone.now()).order_by('-date_posted')[0:7]
    template = 'home/index.html'
    context = {
        'posts': posts,
    }
    if request.method == 'POST':
        email = request.POST['email']
        subscribe(email)   # function to access mailchimp
        messages.success(request, "Thank you for subscribing!")  # message
        posts = Post.objects.filter(
            publish__lte=timezone.now()).order_by('-date_posted')[0:7]
        template = 'home/index.html'
        context = {
            'posts': posts,
        }
        return render(request, "home/index.html", context)
    return render(request, template, context)
