from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Contestant)
admin.site.register(Season)
