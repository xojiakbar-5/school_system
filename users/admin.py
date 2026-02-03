from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'role', 'grade', 'email']
    
    # Yangi foydalanuvchi yaratish formasiga 'role' maydonini qo'shish
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'grade')}),
    )
    
    # Foydalanuvchini tahrirlash formasiga 'role' maydonini qo'shish
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('role', 'grade')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)