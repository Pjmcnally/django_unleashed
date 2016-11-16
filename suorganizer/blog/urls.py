from django.conf.urls import url

from .views import post_list, post_detail

urlpatterns = [
    url(r'$', post_list, name='blog_post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'
    )
]