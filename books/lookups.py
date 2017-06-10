from ajax_select import register, LookupChannel

from students.models import Students
from books.models import Books


@register('firstname')
class FirstnameLookup(LookupChannel):

    model = Students

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        return self.model.objects.filter(firstname__contains=q).order_by('firstname')

    def format_item_display(self, item):
        return u"<span class='firstname'>%s</span>" % item.firstname


@register('title')
class TitleLookup(LookupChannel):

    model = Books

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        return self.model.objects.filter(title__contains=q).order_by('title')

    def format_item_display(self, item):
        return u"<span class='title'>%s</span>" % item.title
