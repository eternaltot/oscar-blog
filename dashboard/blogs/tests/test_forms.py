from oscar.core.loading import get_model

from django.test import TestCase

from .. import forms
from test import factories

Post = get_model('blogs', 'Post')


class TestCreatePostActionForm(TestCase):
    def setUp(self):
        self.form = forms.PostModelForm
        self.post = factories.PostFactory
        self.user = factories.UserFactory(is_superuser=True)

    def test_should_have_field_that_we_expect(self):
        expected = ['title', 'content', 'featured_image',
                    'post_date', 'excerpt', 'author']
        self.assertEquals(expected, self.form.Meta.fields)

    def test_require_field_should_have_check_required(self):
        data = {}
        form = self.form(data=data)
        self.assertFalse(form.is_valid())
        expected_errors = {
            'title': ['This field is required.'],
            'post_date': ['This field is required.'],
            'excerpt': ['This field is required.'],
        }
        self.assertDictEqual(form.errors, expected_errors)

    def test_when_save_should_have_data_in_db(self):
        data = {
            'title': 'post2',
            'post_date': '02/02/2019',
            'excerpt': 'post2',
        }

        form = self.form(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        expect = Post.objects.get(title=data['title'])
        self.assertEquals(expect.title, data['title'])
        self.assertEquals(expect.excerpt, data['excerpt'])
