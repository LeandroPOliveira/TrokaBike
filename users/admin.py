from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

User = get_user_model()


# -----------------------------
# Inline Profile inside User
# -----------------------------
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


# -----------------------------
# Custom User Admin
# -----------------------------
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Unregister default User
admin.site.unregister(User)

# Register new User with Profile inline
admin.site.register(User, UserAdmin)

# Register Profile separately (optional)
admin.site.register(Profile)