"""
views are where you create things to be seen
"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """
    returns what to show in browser when someone goes to request
    """
    return HttpResponse("hello")
