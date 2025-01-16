from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator:
    """
    Генератор для фильтрации транзакций по валюте.

    transactions: список транзакций.
    currency_name: код валюты (usd, USD).
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code.upper():
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Генератор для получения описания транзакций.

    transactions: список транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Генератор для создания номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    start: Начальное значение (включительно), целое число.
    stop: Конечное значение (включительно), целое число.
    Генератор возвращает номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        num = f"{number:016d}"
        yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:16]}"
