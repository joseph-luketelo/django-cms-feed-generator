from django.conf.urls import *
from feed_generator.feeds import RSSFeed
from django.conf.urls import include, url

urlpatterns = url('feed_generator.feeds',
    (r'^rss/$', RSSFeed()),
)
urlpatterns += url('feed_generator.views',
    (r'^get_file/', 'get_file'),
)
