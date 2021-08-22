from django.contrib import admin
from chat.models import Room, User, Message
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (*UserAdmin.fieldsets, ('Дополнительная информация', {'fields': ('age', 'sex', 'avatar')}))
    add_fieldsets = UserAdmin.add_fieldsets
    add_fieldsets[0][1]['fields'] = add_fieldsets[0][1]['fields'] + ('age', 'sex', 'avatar')


# Register your models here.
admin.site.register(Room)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
