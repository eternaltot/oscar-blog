from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

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
        data['categories_formset_class'] = self.categories_formset_class()
        return data

    def form_valid(self, form):
        categories_formset_class = self.categories_formset_class(self.request.POST)
        self.object = form.save()

        if categories_formset_class.is_valid():
            categories_formset_class.instance = self.object
            categories_formset_class.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    template_name = 'dashboard/blogs/blog-create-update.html'
    context_object_name = 'posts'
    model = Post
    form_class = PostModelForm
    categories_formset_class = CategoriesFormset
    success_url = reverse_lazy('blogs-post-list')
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = _("Update")
        context['heading'] = _("Update Post")
        context['categories_formset_class'] = self.categories_formset_class(instance=self.object)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def process_all_forms(self, form):
        formset = self.categories_formset_class(self.request.POST, instance=self.object)
        is_valid = form.is_valid() and formset.is_valid()
        if is_valid:
            return self.forms_valid(form, formset)
        else:
            return self.forms_invalid(form, formset)

    form_valid = form_invalid = process_all_forms

    def forms_valid(self, form, formset):
        self.object = form.save()
        formset.save()
        return super().form_valid(form)

    def forms_invalid(self, form, formset):
        messages.error(self.request,
                       _("Your submitted data was not valid - please "
                         "correct the errors below"))
        ctx = self.get_context_data(form=form)
        ctx['categories_formset_class'] = formset
        return self.render_to_response(ctx)

    def get_success_url(self):
        action = self.request.POST.get('action')
        if action == 'continue':
            return reverse(
                'blog-post-detail', kwargs={"pk": self.object.id})
        else:
            return reverse('blogs-post-list')


class PostDeleteView(generic.DeleteView):
    template_name = 'dashboard/blogs/blog-post-delete.html'
    context_object_name = 'post'
    model = Post
    success_url = reverse_lazy('blogs-post-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['pk'])
