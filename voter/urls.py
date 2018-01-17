"""

"""
#from django.urls import path
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
                path("", views.index, name = "index"),
                path("<int:show_id>", views.show, name = "show" )
              ]
