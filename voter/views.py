"""
views are where you create things to be seen
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Show
# Create your views here.


def index(request):
    """
    returns what to show in browser when someone goes to request
    """
    shows = Show.objects.all()
    return render(request, "voter/home.html", {"shows": shows})

def show(request, show_id):
    show = get_object_or_404(Show, id = show_id)
    return render(request, "voter/show.html", {"show": show})
