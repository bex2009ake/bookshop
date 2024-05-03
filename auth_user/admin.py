from django.contrib import admin
from auth_user.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)