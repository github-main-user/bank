class WrongNumberLengthError(Exception):
    pass


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа.
    Возвращает маску формата: XXXX XX** **** XXXX (X - цифра номера)
    """

    mask = list(str(card_number))  # Преобразовать номер в список символов
    if len(mask) != 16:
        raise WrongNumberLengthError("Номер карты должен состоять из 16 цифр.")

    mask[6:12] = "*" * 6  # "Скрыть" символы с 6 до 12

    # Разбить номер на чанки по 4 символа в каждом
    chunked_mask = ["".join(mask[i : i + 4]) for i in range(0, len(mask), 4)]

    return " ".join(chunked_mask)


def get_mask_account(account_number: int) -> str:
    """
    Функция примимает на вход номер счёта в виде числа.
    Возвращает маску формата: **XXXX (X - цифра номера)
    """

    if len(str(account_number)) != 20:
        raise WrongNumberLengthError("Номер счёта должен состоять из 20 цифр.")

    return f"**{str(account_number)[-4:]}"
