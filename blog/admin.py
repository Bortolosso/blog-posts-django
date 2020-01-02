from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'tittle', 
        'slug', 
        'status', 
        'created_on'
    )
    list_filter = (
        'status',
    )
    search_fields = [
        'tittle',
        'content'
    ]
    prepopulated_fields = {
        'slug': (
            'tittle',
        )
    }
    summernote_fields = (
        'content',
    )

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'body', 
        'post', 
        'created_on', 
        'active'
    )
    list_filter = (
        'active', 
        'created_on'
    )
    search_fields = (
        'name', 
        'email', 
        'body'
    )
    actions = [
        'approve_comments'
    ]

    def approve_comments(self, request, queryset):
        queryset.update(active = True)

admin.site.register(Post, PostAdmin)
