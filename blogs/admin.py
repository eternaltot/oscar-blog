from django.contrib import admin
from oscar.core.loading import get_model

# Register your models here.
Category = get_model('blogs', 'Category')
Post = get_model('blogs', 'Post')
CategoryMapping = get_model('blogs', 'CategoryMapping')


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title',
                    'post_author',
                    'post_date',
                    'create_date',
                    'update_date')
    search_fields = ('post_title', 'post_author__username')
    list_filter = ['post_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoryMapping)
