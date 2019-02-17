import datetime

from oscar.core.loading import get_model, get_class

from django.views import generic

Post = get_model('blogs', 'Post')
Category = get_model('blogs', 'Category')
CategoryMapping = get_model('blogs', 'CategoryMapping')
PostSearchForm = get_class('blogs.forms', 'PostSearchForm')


class BlogIndexView(generic.ListView):
    template_name = 'blogs/blog-list.html'
    model = Post
    paginate_by = 2
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_categories()
        return context

    def get_posts_published(self, queryset):
        return queryset.filter(post_date__lte=datetime.date.today())

    def get_categories(self):
        return Category.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.get_posts_published(queryset)
        queryset = self.apply_search(queryset)
        return queryset

    def apply_search(self, queryset):
        search = self.request.GET.get('search')
        if search is None or search != '':
            return queryset

        queryset = queryset.filter(title__icontains=search)

        return queryset
