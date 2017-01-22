from ajax_select import register, LookupChannel
from .models import Books

@register('title')
class TitleLookup(LookupChannel):

    model = Books

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        return self.model.objects.filter(title__contains=q).order_by('title')

    def format_item_display(self, item):
        return u"<span class='title'>%s</span>" % item.title