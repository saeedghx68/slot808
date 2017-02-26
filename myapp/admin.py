from django.contrib import admin
from myapp.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from myapp.admin_view import *

User = get_user_model()


class MyUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserForm
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('img', 'score', 'total_spin')}),
    )
    # readonly_fields = ('username', )

admin.site.register_view('user-list', view=view_user_list)
admin.site.register(User, MyUserAdmin)
admin.site.register(Awards)
admin.site.register(UserAwards)
