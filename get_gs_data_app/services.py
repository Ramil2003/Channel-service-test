import gspread
from django.conf import settings
from typing import Any

from .models import SheetsData
from .parsing_currency import get_current_dollar


def authentication() -> Any:
    """
    User authentication

    :return: Any
    :rtype: Any
    """
    return gspread.service_account(filename=settings.JSON_CONFIG)


def get_data_from_gs() -> list[dict]:
    """
    Get data from Google Sheets (gs). \n
    We authenticate user. \n
    Open our page in Google Sheets. \n
    Get and return all data from gs like list[dict].

    :return: return all data from gs list[dict]
    :rtype: list[dict]
    """
    auth = authentication()
    sh = auth.open('Copy of test')
    return sh.sheet1.get_all_records()


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
    SheetsData.objects.update_or_create(order_num=order_num, cost_dol=cost_dol, cost_rub=cost_dol*dollar,
                                               delivery_time=delivery_time)



# TODO:
# 1. upload_data_to_db
# 2. work with templates
# 4. Add celery and redis to docker-compose
# 5. Add task for celery

