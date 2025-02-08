import pandas as pd


def load_transactions_csv(file_path: str) -> list[dict]:
    """
    Возвращает список транзакций из переданного csv файла.
    Столбцы должны быть разделены с помощью точки с запятой (;).
    """

    df = pd.read_csv(file_path, delimiter=";")
    return df.to_dict(orient="records")


def load_transactions_excel(file_path: str) -> list[dict]:
    """
    Возвращает список транзакций из переданного excel файла.
    """

    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
