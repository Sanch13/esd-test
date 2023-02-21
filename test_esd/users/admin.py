from django.contrib import admin
from users.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'tab_number',
                    'is_active')

