import re

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from cms.models.pagemodel import Page
from feed_generator.models import PageRSSFeed
from feed_generator.settings import exclude_keyword, feed_limit


def _page_in_rss(page):
    try:
        return not PageRSSFeed.objects.get(page=page).not_visible_in_feed
    except PageRSSFeed.DoesNotExist:
        pass
    return True

    

class CustomFeedGenerator(Rss201rev2Feed):
    """ Custom feed generator. Created to add extra information to the rss feed page"""
    
    def rss_attributes(self):
        """ Overriden this method to add media namespace(needed because we added media tags) """
        return {u"version": self._version,
                u"xmlns:media": u"http://search.yahoo.com/mrss/",
                "xmlns:atom": u"http://www.w3.org/2005/Atom"
                }

    def add_item_elements(self, handler, item):
        super(CustomFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u"media:description", item['short_description'])
        handler.addQuickElement(u"tags", item['tags'])
        handler.addQuickElement(u"media:thumbnail", attrs={'url':item['image_url']})

class RSSFeed(Feed):
    Sitetitle = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Site.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return item.get_absolute_url()

