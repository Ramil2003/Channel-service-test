from celery import shared_task

from .parsing_currency import _get_current_dollar
from .services import _open_n_get_data_from_gs
from .models import SheetsData


@shared_task()
def upload_data_to_db() -> None:
    """
    Upload data to DB

    :return: None
    :rtype: None
    """
    data = _open_n_get_data_from_gs()
    dollar = _get_current_dollar()
    for d in data:
        SheetsData.objects.bulk_create([SheetsData(order_num=d['заказ №'],
                                                   cost_dol=d['стоимость,$'],
                                                   cost_rub=round(float(d['стоимость,$'] * dollar), 1),
                                                   delivery_time=d['срок поставки'])])

# Доделать загрузку в бд
