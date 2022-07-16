from celery import app

from .parsing_currency import get_current_dollar
from .services import get_data_from_gs
from .models import SheetsData


@app.task
def upload_data_to_db() -> None:
    """
    Upload data to DB

    :return: None
    :rtype: object
    """
    data = get_data_from_gs()
    dollar = get_current_dollar()
    order_num = (d['заказ №'] for d in data)
    cost_dol = (d['стоимость,$'] for d in data)
    delivery_time = (d['срок поставки'] for d in data)
    SheetsData.objects.update_or_create(order_num=order_num, cost_dol=cost_dol, cost_rub=cost_dol * dollar,
                                        delivery_time=delivery_time)
