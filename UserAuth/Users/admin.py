from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Users.models import User

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    list_display = ["id", "email", "name", "referral_code", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "referral_code"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "referral_code", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "name"]
    ordering = ["email", "id"]
    filter_horizontal = []

# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
