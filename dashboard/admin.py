from django.contrib import admin
from .models import CustomSession

from django.contrib.sessions.models import Session

admin.site.register(CustomSession)
admin.site.register(Session)


