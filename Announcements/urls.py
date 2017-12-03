from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.announcements, name='announcements-home'),
	url(r'^addannouncement/$', views.add_announcement, name='add-announcement'),
	url(r'^deleteannouncement/(?P<announcementid>\d+)/$', views.delete_announcement, name='delete-announcement')
]
