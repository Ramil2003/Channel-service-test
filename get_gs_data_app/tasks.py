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
    qs1 = SheetsData.objects.all()
    for d in data:
        SheetsData.objects.update_or_create(order_num=d.get('заказ №', 0),
                                            cost_dol=d.get('стоимость,$', 0),
                                            cost_rub=round(float(d.get('стоимость,$', 0) * dollar), 1) or 0,
                                            delivery_time=d.get('срок поставки', "00.00.00"))
        qs2 = SheetsData.objects.filter(order_num=d.get('заказ №', 0),
                                        cost_dol=d.get('стоимость,$', 0),
                                        cost_rub=round(float(d.get('стоимость,$', 0) * dollar), 1) or 0,
                                        delivery_time=d.get('срок поставки', "00.00.00"))
    if qs1.difference(qs2):
        qs2.delete()
