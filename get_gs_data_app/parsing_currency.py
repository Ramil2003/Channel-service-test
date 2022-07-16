import requests
import xml.etree.ElementTree as ET


def get_current_dollar() -> float:
    """
    Get current dollar from XMl file in https://www.cbr.ru/scripts/XML_daily.asp

    :return: Current dollar
    :rtype: float
    """
    data = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    dollar = ET.fromstring(data.text)
    return float(dollar[10][4].text.replace(',', '.'))