#from django.urls import path
from django.conf.urls import url

from posts.views import PostsListView, PostsView

helper_patterns = [
    url(r'^posts/$', PostsListView.as_view(), name='posts'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostsView.as_view(), name='get_posts')
    #
] 

urlpatterns = helper_patterns

