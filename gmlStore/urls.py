from django.conf.urls.defaults import *

urlpatterns = patterns('mapbin.gmlStore.views',
    (r'^$', 'index'),
    (r'^store$', 'store'),
    (r'^(?P<gml_id>\d+)$', 'info'),
    (r'^(?P<gml_id>\d+)/get$', 'get'),
    (r'^(?P<gml_id>\d+)/info$', 'info'),
)
