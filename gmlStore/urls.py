from django.conf.urls.defaults import *

urlpatterns = patterns('mapbin.gmlStore.views',
    (r'^$', 'index'),
    (r'^(?P<gml_id>\d+)$', 'info'),
    (r'^(?P<gml_id>\d+)/get$', 'get'),
    (r'^(?P<gml_id>\d+)/info$', 'info'),
)
