from django.contrib import admin
from myapp.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from myapp.admin_view import *
from django import forms

User = get_user_model()


class MyUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserForm
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('img', 'score', 'win', 'chance_of_gift', )}),
    )
    # readonly_fields = ('username', )


class LotteryAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


class AboutAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('alt','cat_id')
    search_fields = ('alt',)
    list_filter = ('cat_id',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category)
admin.site.register_view('user-list', view=view_user_list)
admin.site.register(User, MyUserAdmin)
admin.site.register(Lottery, LotteryAdmin)
admin.site.register(Awards)
admin.site.register(UserAwards)
admin.site.register(About, AboutAdmin)
admin.site.register(Goals)
admin.site.register(Points)
admin.site.register(News)
