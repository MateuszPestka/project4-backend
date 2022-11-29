from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from django.contrib import admin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
