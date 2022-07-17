import gspread
from django.conf import settings
from typing import Any


def _authenticate() -> Any:
    """
    User authentication

    :return: Any
    :rtype: Any
    """
    return gspread.service_account(filename=settings.JSON_CONFIG)


def _open_n_get_data_from_gs() -> list[dict]:
    """
    We authenticate user. \n
    Open our page in Google Sheets. \n
    Get and return all data from gs like list[dict].

    :return: return all data from gs list[dict]
    :rtype: list[dict]
    """
    auth = _authenticate()
    sh = auth.open('Copy of test')
    return sh.sheet1.get_all_records()

# TODO:
# 1. upload_data_to_db COMPLETE
# 2. work with templates
# 4. Add celery and redis to docker-compose COMPLETE
# 5. Add task for celery COMPLETE

