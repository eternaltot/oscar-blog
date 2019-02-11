from django.urls import reverse_lazy
from django.views import generic
from blogs.models import Post
from .forms import PostModelForm
from .formsets import CategoriesFormset


class PostListView(generic.ListView):
    template_name = 'dashboard/blogs/blogs-post-list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostCreateView(generic.CreateView):
    template_name = 'dashboard/blogs/blog-create-update.html'
    context_object_name = 'posts'
    model = Post
    form_class = PostModelForm
    categories_formset_class = CategoriesFormset
    success_url = reverse_lazy('blogs-post-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category_formset'] = self.categories_formset_class()
        return data

    def form_valid(self, form):
        category_formset = self.categories_formset_class(self.request.POST)
        self.object = form.save()

        if category_formset.is_valid():
            category_formset.instance = self.object
            category_formset.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    template_name = 'dashboard/blogs/blog-create-update.html'
    context_object_name = 'posts'
    model = Post
    form_class = PostModelForm
    categories_formset_class = CategoriesFormset
    success_url = reverse_lazy('blogs-post-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category_formset'] = self.categories_formset_class()
        return data

    def form_valid(self, form):
        category_formset = self.categories_formset_class(self.request.POST)
        self.object = form.save()

        if category_formset.is_valid():
            category_formset.instance = self.object
            category_formset.save()
        return super().form_valid(form)
