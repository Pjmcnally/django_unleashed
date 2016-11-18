from django.conf.urls import url

from .views import PostCreate, PostList, post_detail

urlpatterns = [
    url(
        r'^$',
        PostList.as_view(),
        name='blog_post_list'
        ),
    url(
        r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'
    ),
    url(
        r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'
    ),
]
