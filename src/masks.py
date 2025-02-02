import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class WrongNumberLengthError(Exception):
    pass


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа.
    Возвращает маску формата: XXXX XX** **** XXXX (X - цифра номера)
    """

    logger.info(f"Функция get_mask_card_number вызвана с аргуметом: {card_number}")

    if not isinstance(card_number, int):
        logger.error(f"Передан неверный тип данных: {type(card_number)}")
        raise TypeError("Номер карты должен быть числом.")

    mask = list(str(card_number))  # Преобразовать номер в список символов
    if len(mask) != 16:
        logger.error(f"Неверная длина номера карты: {len(mask)}")
        raise WrongNumberLengthError("Номер карты должен состоять из 16 цифр.")

    mask[6:12] = "*" * 6  # "Скрыть" символы с 6 до 12

    # Разбить номер на чанки по 4 символа в каждом
    chunked_mask = ["".join(mask[i : i + 4]) for i in range(0, len(mask), 4)]

    masked_card = " ".join(chunked_mask)
    logger.info(f"Замаскированнй номер карты: {masked_card}")

    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Функция примимает на вход номер счёта в виде числа.
    Возвращает маску формата: **XXXX (X - цифра номера)
    """

    logger.info(f"Функция get_mask_account вызвана с аргуметом: {account_number}")

    if not isinstance(account_number, int):
        logger.error(f"Передан неверный тип данных: {type(account_number)}")
        raise TypeError("Номер счёта должен быть числом.")

    if len(str(account_number)) != 20:
        logger.error(f"Неверная длина номера счёта: {len(str(account_number))}")
        raise WrongNumberLengthError("Номер счёта должен состоять из 20 цифр.")

    masked_account = f"**{str(account_number)[-4:]}"
    logger.info(f"Замаскированнй номер счёта: {masked_account}")

    return masked_account
