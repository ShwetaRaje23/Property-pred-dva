from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'prop_pred_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'prop_pred_server.views.login')
    url(r'^$', 'prop_pred_server.views.login'),
    url(r'^index/$', 'prop_pred_server.views.index', name='index'),
    url(r'^map/$', 'prop_pred_server.views.maps', name='map')
]
