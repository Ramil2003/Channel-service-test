from typing import Any

from django.views.generic import ListView
from django.db.models import Sum

from .models import SheetsData


class DataListView(ListView):
    model = SheetsData
    context_object_name = 'data_list'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs) -> Any:
        """
        Return context with sum of cost all products

        :return: Any
        :rtype: Any
        """
        context = super(DataListView, self).get_context_data()
        context['total'] = SheetsData.objects.aggregate(Sum('cost_rub'))['cost_rub__sum']
        return context
