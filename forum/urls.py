from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #show list
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), #show post
    url(r'^post/new/$', views.post_new, name='post_new'), #create new post
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), #edit post
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'), #add comment


    url(r'^destinations/$', views.post_list_dest, name='post_list_dest'),
    url(r'^destinations/post/(?P<pk>\d+)/$', views.post_detail, name='dest_post_detail'),
    url(r'^destinations/post/new/$', views.dest_post_new, name='dest_post_new'),

    url(r'^practical/$', views.post_list_prac, name='post_list_prac'),

    url(r'^other/$', views.post_list_other, name='post_list_other'),


    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
