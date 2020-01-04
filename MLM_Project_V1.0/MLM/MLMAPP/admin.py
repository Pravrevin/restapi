from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyUser

# Register your models here.

class UserAdmin(BaseUserAdmin):

	list_display = ('username','email','number','refercode','is_admin')
	list_filter = ('is_admin',)

	fieldsets = (
			(None, {'fields': ('username','email','number','refercode','password')}),
			('Permissions', {'fields': ('is_admin',)})
		)
	search_fields = ('username','email','number')
	ordering = ('username','email','number')

	filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)


admin.site.unregister(Group)