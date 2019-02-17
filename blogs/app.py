from oscar.core.application import Application
from oscar.core.loading import get_class

from django.conf.urls import url


class BlogApplication(Application):
    name = 'blogs'

    blog_index_view = get_class('blogs.views', 'BlogIndexView')

    def get_urls(self):
        urls = [
            url(r'^$',
                self.blog_index_view.as_view(), name='blog-list'),
        ]
        return self.post_process_urls(urls)


application = BlogApplication()
