import re

from cms.models.pagemodel import Page
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from feed_generator.models import PageRSSFeed
from feed_generator.settings import exclude_keyword, feed_limit


class RSSFeed(Feed):
    link = "/"
    description = "Updates on changes and additions to police beat central."

    def __init__(self):
        pass
    
    def items(self):
        site = Site.objects.get_current()
        feed_pages = Page.objects.published(site=site).order_by("-publication_date")
        return [feed_page for feed_page in feed_pages if _page_in_rss(feed_page)][
            :feed_limit
        ]

    def item_title(self, item):
        # SEO page title or basic title
        title = item.get_page_title() or item.get_title()
        return title[:60] if title else ""

    def item_description(self, item):
        # SEO page description
        return item.get_meta_description()[:400] if item.get_meta_description() else ""

    def item_link(self, item):
        # Page url
        return item.get_absolute_url()

