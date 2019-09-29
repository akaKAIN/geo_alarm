from django.contrib import admin

# Register your models here.
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'phone',
        'address',
    ]


admin.site.register(User, UserAdmin)
