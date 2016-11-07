#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('maps.urls')),
    # ... your url patterns
]
