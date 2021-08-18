from django.contrib import admin
from chat.models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (*UserAdmin.fieldsets, ('Дополнительная информация', {'fields': ('age', 'sex', 'avatar', 'room')}))
    add_fieldsets = UserAdmin.add_fieldsets
    add_fieldsets[0][1]['fields'] = add_fieldsets[0][1]['fields'] + ('age', 'sex', 'avatar', 'room')


# Register your models here.
admin.site.register(Room)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
