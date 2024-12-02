from django.contrib import admin
from .models import Response

# Register your models here.

# admin.site.register(Profile)
@admin.register(Response)
class Response(admin.ModelAdmin):
    list_display = ('category','question','response1')
