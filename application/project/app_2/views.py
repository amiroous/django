from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Django App 2 >> Index')
