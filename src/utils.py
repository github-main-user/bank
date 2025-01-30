import json
import os


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
