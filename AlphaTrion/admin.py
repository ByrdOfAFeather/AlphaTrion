from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from UserProfile.models import Student


class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (StudentInLine, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)