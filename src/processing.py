from datetime import datetime
from typing import Optional


def filter_by_state(operations: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях.
    Отбирает только словари, в которых содержимое state соотвествует переданному.
    Возвращает отфильтрованный список словарей обратно.
    """

    return [op for op in operations if op.get("state", "") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях.
    Возвращает новый отсортированный список словарей обратно.
    По умолчанию сортировка по убыванию.
    """

    return sorted(
        operations,
        key=lambda op: datetime.fromisoformat(op.get("date", "1970-01-01")),
        reverse=reverse,
    )
