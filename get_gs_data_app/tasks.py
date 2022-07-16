from celery import shared_task

from .parsing_currency import get_current_dollar
from .services import get_data_from_gs
from .models import SheetsData


@shared_task()
def upload_data_to_db() -> None:
    """
    Upload data to DB

    :return: None
    :rtype: object
    """
    data = get_data_from_gs()
    dollar = get_current_dollar()
    order_num = [d['заказ №'] for d in data]
    cost_dol = [d['стоимость,$'] * dollar for d in data]
    delivery_time = [d['срок поставки'] for d in data]
    pass
