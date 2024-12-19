def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа.
    Возвращает маску формата: XXXX XX** **** XXXX (X - цифра номера)
    """

    mask = list(str(card_number))  # Преобразовать номер в список символов
    mask[6:12] = "*" * 6  # "Скрыть" символы с 6 до 12

    # Разбить номер на чанки по 4 символа в каждом
    chunked_mask = ["".join(mask[i: i + 4]) for i in range(0, len(mask), 4)]

    return " ".join(chunked_mask)


def get_mask_account(account_number: int) -> str:
    """
    Функция примимает на вход номер счёта в виде числа.
    Возвращает маску формата: **XXXX (X - цифра номера)
    """
    return f"**{str(account_number)[-4:]}"
