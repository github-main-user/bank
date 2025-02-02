import json
import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

load_dotenv()
API_KEY = os.getenv("API_KEY", "")


class APIError(Exception):
    pass


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями или пустой список в случае ошибки.
    """

    logger.info(f"Функция load_transactions вызвана с аргументом {file_path}")

    if not os.path.exists(file_path):
        logger.warning("Файл по переданному пути не существует")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list) and len(data) > 0:
                logger.info("Транзакции из переданного файла успешно загружены")
                return data
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка при обработке файла: {e}")

    logger.info("Переданный файл не содержит ни одной транзакции")
    return []


def _get_exchange_rate_to_rub(currency_code: str) -> float:
    """
    Получает текущий курс валюты к рублю (RUB) через API от "api.apilayer.com".
    """

    BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {"apikey": API_KEY}
    params = {"base": currency_code, "symbols": "RUB"}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:

        data = response.json()
        return float(data["rates"]["RUB"])
    else:
        raise APIError(f"Error with API: {response.text}")


def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Принимает транзакцию в виде словаря и возвращает сумму в рублях.
    Возвращает 0, в случае не корректной транзакции.

    :param transaction (dict):
    :return: сумма транзакции в рублях (float)
    """

    logger.info("В функцию get_transaction_amount_rub была передана транзакция")

    try:
        operation_amount = transaction["operationAmount"]
        amount = float(operation_amount["amount"])
        currency_code = operation_amount["currency"]["code"]
        logger.info(f"Код валюты ({currency_code}) получен")

        exchange_rate = _get_exchange_rate_to_rub(currency_code) if currency_code != "RUB" else 1
        logger.info(f"Получен курс {currency_code} к рублю ({exchange_rate})")

        return amount * exchange_rate
    except (KeyError, ValueError, TypeError):
        logger.error("Передана некорректная транзакция")
    except APIError:
        logger.error("Ошибка с api сервисом")

    return 0
