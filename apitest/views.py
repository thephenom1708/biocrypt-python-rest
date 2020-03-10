import json

import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from registration.models import User
from .models import Share, UserShareMapping


def index(request):
    return HttpResponse("Hello World");


@csrf_exempt
def testing(request):
    share_number = request.POST.get('share_number', None)
    username = request.POST.get('username', None)
    share_data = request.POST.get('share_data', None)
    context = {
        'username': username
    }
    address = "http://192.168.43.86:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']

    share = Share()
    share.create_new_share(share_number, share_data)
    share.save()

    user_share_mappings = UserShareMapping.objects.filter(user_id=user_id)
    if len(user_share_mappings) == 0:
        new_user_share_mapping = UserShareMapping()
        new_user_share_mapping.user_id = user_id
        new_user_share_mapping.save()

    user_share_mapping = UserShareMapping.objects.get(user_id=user_id)
    user_share_mapping.shares.add(share)
    user_share_mapping.save()

    return HttpResponse("Share Received")


@csrf_exempt
def returnShares(request):
    username = request.POST.get('username', None)
    context = {
        'username': username
    }
    address = "http://192.168.43.86:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']

    shares = UserShareMapping.objects.get(user_id=user_id).shares.all()

    shareList = []
    for share in list(shares):
        shareList.append({
            'share_number': share.share_number,
            'share_data': share.share_data
        })
    context = {
        'shares': shareList
    }
    return JsonResponse(context)


@csrf_exempt
def delete_shares(request):
    Share.objects.all().delete()
    return HttpResponse("")


@csrf_exempt
def delete_user_mappings(request):
    UserShareMapping.objects.all().delete()
    return HttpResponse("")


@csrf_exempt
def delete_users(request):
    User.objects.all().delete()
    return HttpResponse("")
