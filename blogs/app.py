from oscar.core.application import Application
from oscar.core.loading import get_class

from django.conf.urls import url


class BlogApplication(Application):
    name = 'blog'

    # blog_index_view = get_class('blog.views', 'BlogIndexView')
    # blog_detail_view = get_class('blog.views', 'BlogDetailView')
    # blog_category_list = get_class('blog.views', 'BlogCategoryView')

    def get_urls(self):
        urls = [
            # url(r'^$',
            #     self.blog_index_view.as_view(), name='blog-list'),
            # url(r'^detail/(?P<slug>[\w-]*)/$',
            #     self.blog_detail_view.as_view(), name='blog-detail'),
            # url(r'^category/(?P<slug>[\w-]*)/$',
            #     self.blog_category_list.as_view(), name='blog-category-list'),
        ]
        return self.post_process_urls(urls)


application = BlogApplication()