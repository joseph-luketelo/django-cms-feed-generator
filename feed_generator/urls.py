from django.conf.urls import *
from feed_generator.feeds import RSSFeed
from django.conf.urls import include, url
from feed_generator.feeds import RSSFeed
from feed_generator.views import get_file

urlpatterns = url('r'^rss/$',RSSFeed,name='rssfeed')
urlpatterns += url('r'^get_file/',get_file,name='get_file')

