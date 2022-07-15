from django.views.generic import ListView

from .models import SheetsData


class DataListView(ListView):
    model = SheetsData
    context_object_name = 'datas'
    template_name = 'index.html'

