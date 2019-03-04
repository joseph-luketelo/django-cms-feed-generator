from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.contrib.sites.models import Site

class RSSFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def __init__(self, name):
        self.name = name
        print("IN INIT METHOD")
        
    def items(self):
        return Site.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])


