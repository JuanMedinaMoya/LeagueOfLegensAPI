from django.contrib import admin

# Register your models here.
from .models import Friend, User

admin.site.register(User)
admin.site.register(Friend)