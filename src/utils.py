import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY', '')


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями или пустой список в случае ошибки.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, IOError):
        pass

    return []


def _get_exchange_rate_to_rub(currency_code: str) -> float:
    """
    Получает текущий курс валюты к рублю (RUB) через API от "api.apilayer.com".
    """
    if currency_code == "RUB":
        return 1.0  # Если валюта уже в рублях, курс 1:1

    BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'

    headers = {'apikey': API_KEY}
    params = {"base": currency_code, "symbols": "RUB"}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["rates"]["RUB"]
    else:
        raise ValueError(f"Error with API: {response.text}")


def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Принимает транзакцию в виде словаря и возвращает сумму в рублях.
    Возвращает 0, в случае не корректной транзакции.

    :param transaction (dict):
    :return: сумма транзакции в рублях (float)
    """
    try:
        operation_amount = transaction['operationAmount']
        amount = float(operation_amount['amount'])
        currency_code = operation_amount['currency']['code']

        exchange_rate = _get_exchange_rate_to_rub(currency_code)
        return amount * exchange_rate
    except (KeyError, ValueError, TypeError):
        return 0
