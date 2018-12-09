# -*- coding: utf-8 -*-

# Create your views here.
#
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World.You are Sample App")

