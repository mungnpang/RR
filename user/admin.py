from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import UserModel

# Register your models here.

admin.site.register(UserModel)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname,")}),)
