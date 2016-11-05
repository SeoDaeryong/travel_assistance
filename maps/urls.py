from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'ajax/add', views.ajax_add, name='ajax_add'),
    url(r'ajax/delete', views.ajax_delete, name='ajax_delete'),
    url(r'ajax/capital', views.ajax_capital, name='ajax_capital'),
    url(r'gmaps', views.load_gmaps, name='load_gmaps'),
    url(r'^place/(?P<pk>[0-9]+)/$', views.place_detail, name='place_detail'),
]
