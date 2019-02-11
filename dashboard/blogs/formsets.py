from django.forms.models import inlineformset_factory

from .forms import CategoriesModelForm
from blogs.models import Post, CategoryMapping


CategoriesFormset = inlineformset_factory(
    Post, CategoryMapping, form=CategoriesModelForm, extra=2)
