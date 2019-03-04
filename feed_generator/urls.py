from django.conf.urls import *
from feed_generator.feeds import RSSFeed
from django.conf.urls import include, url
from feed_generator.feeds import RSSFeed
from feed_generator.views import get_file

urlpatterns = url('feed_generator.feeds', (r'^rss/$', RSSFeed()),)


