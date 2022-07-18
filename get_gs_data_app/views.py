from django.views.generic import ListView
from django.db.models import Sum

from .models import SheetsData


class DataListView(ListView):
    model = SheetsData
    context_object_name = 'data_list'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DataListView, self).get_context_data()
        context['total'] = SheetsData.objects.aggregate(Sum('cost_rub'))
        return context
