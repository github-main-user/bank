from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator:
    """
    Возвращает итератор транзакций, где валюта операции соответствует заданной.

    :param transactions: список словарей с транзакциями
    :param currency_code: код валюты для фильтрации (например, "USD")
    :return: итератор с отфильтрованными транзакциями
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """
    Генератор для получения описания транзакций.

    transactions: список транзакций.
    """
    return (transaction.get("description", "") for transaction in transactions)


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
