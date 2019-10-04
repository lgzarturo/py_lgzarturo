from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _

from articles.models import Article


class ArticleFeed(Feed):
    title = _('Webdeveloperhints.com')
    description = _('Artículos sobre desarrollo y tecnología')
    link = '/blog/feed.xml'

    def items(self):
        return Article.objects.filter(is_draft=False)

    def item_description(self, item):
        return item.excerpt
