from oscar.core.loading import get_model

from django import forms
from django.utils.translation import ugettext_lazy as _

Category = get_model('blogs', 'Category')
CategoryMapping = get_model('blogs', 'CategoryMapping')
Post = get_model('blogs', 'Post')


class PostSearchForm(forms.Form):
    name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'placeholder': _('Search Post')}))
