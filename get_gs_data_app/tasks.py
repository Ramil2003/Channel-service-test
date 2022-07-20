from celery import shared_task

from .parsing_currency import _get_current_dollar
from .services import _open_n_get_data_from_gs
from .models import SheetsData


@shared_task()
def work_with_db() -> None:
    """
    Get data from Google Sheets from _open_n_get_data_from_gs
    Get current dollar from _get_current_dollar
    And work with data in db (CUD)

    :return: None
    :rtype: None
    """
    data = _open_n_get_data_from_gs()
    dollar = _get_current_dollar()
    SheetsData.objects.all().delete()
    for d in data:
        SheetsData.objects.create(order_num=d.get('заказ №', 0),
                                  cost_dol=d.get('стоимость,$', 0),
                                  cost_rub=d.get('стоимость,$', 0) * dollar,
                                  delivery_time=d.get('срок поставки', "00.00.00"))
    data.clear()
