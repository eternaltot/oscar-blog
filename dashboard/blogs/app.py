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
            # url(r'^blogs/post/create/$',
            #     self.post_create_view.as_view(), name='blog-post-create'),
            # url(r'^blogs/post/detail/(?P<pk>\d+)/$',
            #     self.post_detail_update_view.as_view(), name='blog-post-detail'),
            # url(r'^blogs/post/delete/(?P<pk>\d+)/$',
            #     self.post_delete_view.as_view(), name='blog-post-delete'),

            # # Blog Categories
            # url(r'^blogs/categories/$',
            #     self.post_category_list_view.as_view(), name='blog-category-list'),
            # url(r'^blogs/categories/create/$',
            #     self.post_category_create_view.as_view(), name='blog-category-create'),
            # url(r'^blogs/categories/detail/(?P<pk>\d+)/$',
            #     self.post_category_detail_update_view.as_view(), name='blog-category-detail'),
            # url(r'^blogs/categories/delete/(?P<pk>\d+)/$',
            #     self.post_category_delete_view.as_view(), name='blog-category-delete')
        ]
        return self.post_process_urls(urls)


application = BlogDashboardApplication()
