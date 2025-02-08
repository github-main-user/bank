import re
from collections import Counter
from datetime import datetime
from typing import Optional


def filter_by_state(operations: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях.
    Отбирает только словари, в которых содержимое state соотвествует переданному.
    Возвращает отфильтрованный список словарей обратно.
    """

    if not isinstance(operations, list):
        raise TypeError("Переданный аргумент не является итерируемым.")

    filtred_list = []
    for op in operations:
        if not isinstance(op, dict):
            raise TypeError("Элемент списка не является словарём.")

        if op.get("state", "") == state:
            filtred_list.append(op)

    return filtred_list


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях.
    Возвращает новый отсортированный список словарей обратно.
    По умолчанию сортировка по убыванию.
    """

    if not isinstance(operations, list):
        raise TypeError("Переданный аргумент не является итерируемым.")

    for op in operations:
        if not isinstance(op, dict):
            raise TypeError("Элемент списка не является словарём.")

    return sorted(
        operations,
        key=lambda op: datetime.fromisoformat(op.get("date", "1970-01-01")),
        reverse=reverse,
    )


def filter_by_description(operations: list[dict], pattern: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    Использует регулярные выражения для поиска, поиск независит от регистра.
    """

    new_operations = []

    for operation in operations:
        if re.search(pattern, operation.get("description", ""), flags=re.IGNORECASE):
            new_operations.append(operation)

    return new_operations


def count_operations_by_category(operations: list[dict], categories: list[str]) -> dict:
    """
    Фукнция принимает список словарей с данными о банковских операциях и список категорий.
    Возвращает словарь в котором ключи - это название категорий,
    а значения - это количество операций в каждой категории.
    """
    matched_categories = [
        operation.get("description", "") for operation in operations if operation.get("description" in categories)
    ]

    return dict(Counter(matched_categories))
