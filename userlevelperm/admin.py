from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post,User
class UserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": (
            # "username",
            "email", "password","role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions","firebase_token","created_gps","device_id",),}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions","role","firebase_token","created_gps","device_id"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    def __str__(self):
        return self.email
# Register your models here.
admin.site.register(Post)

admin.site.register(User,UserAdmin)