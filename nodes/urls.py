from django.conf.urls import patterns, url

from .views import TitleListView, NodeListView, NodeCreateView, TitleCreateView


urlpatterns = patterns('',
    url(r'^title/(?P<pk>\d+)/$', NodeListView.as_view(), name='title'),
    url(r'^$', TitleListView.as_view(), name='list'),

    url(r'^title-create/$', TitleCreateView.as_view(), name='titlecreate'),
    url(r'^node-create/(?P<pk>\d+)/$', NodeCreateView.as_view(), name='nodecreate'),
)
