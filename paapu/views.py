from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def motu(request):
    return HttpResponse('Hello Motuuu')