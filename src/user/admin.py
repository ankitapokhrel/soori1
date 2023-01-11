from django.contrib import admin
from src.user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'email', 'name', 'address', 'contact_info', 'is_admin']
    fieldsets=(
        ('User Credentials', {'fields':('email', 'password',)}),
        ('Personal info', {'fields':('name', 'address', 'contact_info',)}),
        ('Permissions', {'fields':('is_admin',)}),
    )

