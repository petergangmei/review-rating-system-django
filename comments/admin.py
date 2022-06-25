from django.contrib import admin
from .models import *
# Register your models here.

class filter(admin.ModelAdmin):
    list_display = ('author','stars','posted_at',)
admin.site.register(Review,filter)