import gspread

from typing import Any

from django.conf import settings
from .models import SheetsData


def authentication() -> Any:
    """
    User authentication

    :return: Any
    :rtype: Any
    """
    return gspread.service_account(filename=settings.JSON_CONFIG)

