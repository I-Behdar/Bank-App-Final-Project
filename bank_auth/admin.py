from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BankUser


class BankUserAdmin(UserAdmin):
    model = BankUser
    ordering = ["-date_joined"]
    list_display = ["email", "first_name", "last_name", "is_active", "is_staff", "is_admin"]
    list_filter = ["email"]
    filter_horizontal = []
    search_fields = ["email", "first_name", "last_name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(BankUser, BankUserAdmin)
