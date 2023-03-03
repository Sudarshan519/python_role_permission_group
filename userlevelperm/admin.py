from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  ApiErrorLog, Banners, Post, Profession, ResidenceStatus,  User
class UserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff",# "is_active",
                    'account_type','email_verified')
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username","email", "password","role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions","firebase_token","created_gps","device_id","account_type","email_verified"),}),
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

class ApiErrorLogAdmin(admin.ModelAdmin):
    
    model:ApiErrorLog
    list_display = ('platform','label',"funcName","created_at","errorMsg","device_id")
    list_filter = ("platform", "created_at", "device_id",)
# Register your models here.
admin.site.register(Post)

admin.site.register(User,UserAdmin)
admin.site.register(ResidenceStatus)
admin.site.register(Profession)
admin.site.register(ApiErrorLog,ApiErrorLogAdmin)



class BannersAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']
    list_display = ['title', 'img_preview']
admin.site.register(Banners,BannersAdmin)
admin.site.site_header='Clone RPS Remit'
