from django.core.urlresolvers import reverse
from test import factories, test_mixins
from oscar.core.compat import get_user_model
from blogs.models import Post
User = get_user_model()


class TestBlogIndexView(test_mixins.WebTestCase):
    def setUp(self):
        print(User.objects.all())
        self.user = factories.UserFactory()
        self.blog_post = factories.PostWithCategoryFactory()
        self.blog_post_2 = factories.PostWithCategoryFactory()
        # factories.PostWithCategoryFactory()
        self.blog_list_url = reverse('blogs-post-list')

    def test_should_have_data(self):
        self.login_as_super_user()
        response = self.client.get(self.blog_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['posts'],
            [
                '<Post: {}>'.format(self.blog_post.title),
                '<Post: {}>'.format(self.blog_post_2.title)
            ]
        )


class TestBlogCreateView(test_mixins.WebTestCase):
    def setUp(self):
        self.url_list_view = reverse('blogs-post-list')
        self.url_create_view = reverse('blog-post-create')

        self.user = factories.UserFactory(is_staff=True)
        self.blog_category = factories.CategoryFactory()

    def test_post_data_to_create_view_should_have_data_in_db(self):
        self.login_as_super_user()

        data = {
            'title': 'Post Test View',
            'content': 'Content Test View',
            'author': self.user.id,
            'excerpt': 'excerpt',
            'featured_image': '',
            'post_date': '02/02/2019',
            'categorymapping_set-TOTAL_FORMS': '2',
            'categorymapping_set-INITIAL_FORMS': '0',
            'categorymapping_set-MIN_NUM_FORMS': '0',
            'categorymapping_set-MAX_NUM_FORMS': '1000',
            'categorymapping_set-0-category': self.blog_category.id,
            'categorymapping_set-0-abstractcategorymapping_ptr': '',
            'categorymapping_set-0-post': '',
            'categorymapping_set-1-category': '',
            'categorymapping_set-1-abstractcategorymapping_ptr': '',
            'categorymapping_set-1-post': '',
            'action': 'save'
        }
        response = self.client.post(self.url_create_view,
                                    data=data, follow=True)
        self.assertRedirects(response, self.url_list_view)

        expect_post = Post.objects.get(title=data['title'])
        self.assertEqual(expect_post.title, data['title'])

        expect_post_categories = expect_post.categories.all()
        self.assertQuerysetEqual(
            expect_post_categories,
            ['<Category: {}>'.format(
                self.blog_category.name)]
        )


class TestBlogUpdateView(test_mixins.WebTestCase):
    def setUp(self):

        self.blog_category1 = factories.CategoryFactory()
        self.blog_category2 = factories.CategoryFactory()
        self.blog_post_with_category = factories.PostWithCategoryFactory(
            post_category1__category=self.blog_category1,
            post_category2__category=self.blog_category2)

        self.blog_list_url = reverse('blogs-post-list')

    def test_should_have_edit_post_when_user_is_staff(self):
        self.login_as_super_user()

        response = self.client.get(self.blog_post_with_category.get_absolute_url())
        self.assertContains(response, 'Edit this post')

