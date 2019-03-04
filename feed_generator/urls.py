from django.conf.urls import *
from feed_generator.feeds import RSSFeed
from django.conf.urls import include, url
from django.urls import path
from feed_generator.feeds import RSSFeed
from feed_generator.views import get_file

path('rss/$', RSSFeed()),
path('get_file/', get_file()),

