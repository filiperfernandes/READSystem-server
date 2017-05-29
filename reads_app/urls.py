from django.conf.urls import url

from . import views

app_name = 'reads_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/(?P<location_id>[0-9]+)/$', views.location_info, name='location'),
    url(r'^list/location/$', views.list_locations, name='listlocation'),
    url(r'^notification/(?P<notification_id>[0-9]+)/$', views.notification_info, name='notification'),
    url(r'^list/notification/$', views.list_notifications, name='listnotification'),
    url(r'^updatersu/(?P<lat>(-?\d+(?:\.\d+)?))/(?P<lon>(-?\d+(?:\.\d+)?))/$', views.get_rsu_notifications,
        name='updatersu'),
]
