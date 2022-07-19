import requests
import xml.etree.ElementTree as ET

from django.conf import settings


def _get_current_dollar() -> float:
    """
    Get current dollar from XML file in https://www.cbr.ru/scripts/XML_daily.asp

    :return: Current dollar - float
    :rtype: float
    :except requests.exceptions.HTTPError: Returns error if something went wrong
    """
    try:
        data = requests.get(settings.PARSING_SITE)
        if data.status_code == 200:
            dollar = ET.fromstring(data.text)
            return round(float(dollar[10][4].text.replace(',', '.')), 0)
        return 0
    except (requests.exceptions.HTTPError, TypeError, ValueError):
        return 0