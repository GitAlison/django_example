from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import UserProfile

def index(request):
    userprofiles = UserProfile.objects.all()
    ctx = {'userprofiles': userprofiles}
    return render(request, 'index.html', ctx)


def userprofile_json(request):
    up = UserProfile.objects.all()
    data = serializers.serialize('json', up)
    return HttpResponse(data, content_type='application/json')
