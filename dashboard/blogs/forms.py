from django.forms import ModelForm
from blogs.models import Post, Category
from django import forms


class PostModelForm(ModelForm):
    post_date = forms.DateField()

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'featured_image',
            'post_date', 'excerpt', 'author'
            ]


class CategoriesModelForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
