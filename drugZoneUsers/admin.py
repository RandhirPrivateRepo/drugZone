from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from rest_framework.authtoken.admin import Token
# Register your models here.



class CustomUserAdmin(UserAdmin):
	# ...
	fieldsets = (
		('Personal info', {'fields': ('email', 'password','name','phone','role','profileImage')}),
		# ('Important dates', {'fields': ('last_login', 'date_joined')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'user_permissions')}),
    )

admin.site.unregister(Group)
admin.site.unregister(Token)
admin.site.register(CustomUser , CustomUserAdmin)

# admin.site.register(ContactUs)