from django.contrib import admin
from oscar.core.loading import get_model

# Register your models here.
Category = get_model('blogs', 'Category')
Post = get_model('blogs', 'Post')
CategoryMapping = get_model('blogs', 'CategoryMapping')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'post_date',
                    'created_date',
                    'updated_date')
    search_fields = ('title', 'author__username')
    list_filter = ['post_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoryMapping)
