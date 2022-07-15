import gspread
from django.conf import settings
from typing import Any

from .models import SheetsData


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


def upload_data_to_db():
    """

    :rtype: object
    """
    pass

