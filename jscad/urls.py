from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
  'jscad.views',
  url(r'item/(\d+)/([^/]+).jscad','item_source',name='item_source'),
)
