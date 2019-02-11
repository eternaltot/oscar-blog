from oscar.core.application import DashboardApplication

from django.conf.urls import url
from .views import PostListView, PostCreateView


class BlogDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]
    post_list_view = PostListView
    post_create_view = PostCreateView
    # post_create_view = PostCreateView
    # post_detail_update_view = PostDetailUpdateView
    # post_delete_view = PostDeleteView

    # post_category_list_view = CategoryListView
    # post_category_create_view = CategoryCreateView
    # post_category_detail_update_view = CategoryDetailUpdateView
    # post_category_delete_view = CategoryDeleteView

    def get_urls(self):
        urls = [
            # Blog posts
            url(r'^$',
                self.post_list_view.as_view(), name='blogs-post-list'),
            url(r'^create/$',
                self.post_create_view.as_view(), name='blog-post-create'),
        ]
        return self.post_process_urls(urls)


application = BlogDashboardApplication()
