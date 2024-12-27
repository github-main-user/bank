from typing import Optional


def filter_by_state(operations: list[dict], state: Optional[str] = 'EXECUTED') -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях.
    Отбирает только словари, в которых содержимое state соотвествует переданному.
    Возвращает отфильтрованный список словарей обратно.
    """

    return [op for op in operations if op.get('state', '') == state]

