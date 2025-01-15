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
