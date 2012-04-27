from django.conf.urls.defaults import patterns, include, url
from views import writeTopic,readTopic,home
urlpatterns = patterns('',
	(r'^showmytopic$',writeTopic),
	(r'^gettopic$',readTopic),
	(r'^topic$',home)
)
