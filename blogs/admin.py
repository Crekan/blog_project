from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from blogs.models import Posts, Category, Contact, Comment


class PostsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


class PostsAdmin(admin.ModelAdmin):
    form = PostsAdminForm


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)
