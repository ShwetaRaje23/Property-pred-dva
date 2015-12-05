from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^hello/', hello_view),
    #url(r'^action/', action_controller),
    url(r'^map/$', views.inputdata_view, name='maps'),
    url(r'^getdata/$', views.getdata_view),
    url(r'^putmap/$', views.send_data_from_view),
    url(r'^bubble/$', views.showbubble, name='bubble'),
    url(r'^feedback/$', views.collect_feedback),
    url(r'^getfeedbackdata/$', views.feedback_data),
    url(r'^$', views.login)

]