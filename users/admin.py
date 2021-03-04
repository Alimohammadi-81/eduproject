from django.contrib import admin

# Register your models here.
from users.models import RegEmail,UserInfo

admin.site.register(RegEmail)
admin.site.register(UserInfo)
