import json

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from registration.models import User
from .models import Share


def index(request):
    return HttpResponse("Hello Buddy");


@csrf_exempt
def testing(request):
    username = request.POST.get('username', None)
    share_data = request.POST.get('share_data', None)
    context = {
        'username': username
    }
    address = "http://192.168.43.244:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']
    shareId = "1"
    share = Share()
    share.create_new_share(user_id, shareId, share_data)
    share.save()
    return HttpResponse("Share Received")


@csrf_exempt
def returnShares(request):
    username = request.POST.get('username', None)
    context = {
        'username': username
    }
    address = "http://192.168.43.244:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']
    # user_id = get_user_id(username)
    share = Share.objects.filter(user_id=user_id)[0]
    return HttpResponse(share.share_data)


@csrf_exempt
def tp(request):
    #share = Share.objects.filter(user_id="abc")[0]
    #Share.objects.all().delete()
    context = {
        'data': "123"
    }

    return HttpResponse(json.dumps(context))
