from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
  '',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'main.views.home',name='home'),
  url(r'favicon.ico$', 'main.views.redirect',
      {'url': getattr(settings,'FAVICON','/static/favicon.png')}),
  url(r'imgs/busy.gif$', 'main.views.redirect',
      {'url': getattr(settings,'STATIC_URL')+'OpenJSCAD.org/imgs/busy.gif'}),
  url(r'^auth/logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page':'home'}),
  url(r'^auth/', include('django.contrib.auth.urls')),
  url(r'^jscad/', include('jscad.urls')),
  url(r'^(csg.js|openjscad.js|openscad.js)$','main.views.well_this_sucks'),
)

if settings.DEBUG:
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  )
