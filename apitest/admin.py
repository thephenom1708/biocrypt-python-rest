from django.contrib import admin
from .models import Share, UserShareMapping

# Register your models here.

admin.site.register(Share)
admin.site.register(UserShareMapping)