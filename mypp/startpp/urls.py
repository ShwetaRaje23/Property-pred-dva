from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^hello/', hello_view),
    #url(r'^action/', action_controller),
    url(r'^$', views.inputdata_view),
    url(r'^getdata/$', views.getdata_view),
    url(r'^putmap/$', views.send_data_from_view)
]