from .masks import get_mask_account, get_mask_card_number


def _find_first_digit_index(s: str) -> int:
    """
    Принимает строку, возвращает индекс первой встреченной цифры.
    Если цифр нет, возвращает -1.
    """
    for i, ch in enumerate(s):
        if ch.isdigit():
            return i
    return -1


def mask_account_card(card_info: str) -> str:
    """
    Принимает на вход строку содержащую: тип карты или счёт и соответствующий номер.
    Возвращает строку, со скрытым номером карты/счёта.
    """
    # Получить индекс первой встреченной цифры
    first_digit = _find_first_digit_index(card_info)

    # Разделить информацию о карте на тип и номер
    card_type = card_info[:first_digit]
    card_number = card_info[first_digit:]

    # Замаскировать номер, склеить с типом и вернуть
    mask_function = get_mask_account if len(card_number) > 16 else get_mask_card_number
    masked_number = mask_function(int(card_number))
    return card_type + masked_number


def get_date(date_time: str) -> str:
    """
    Принимает строку с датой в формате: "2024-03-11T02:26:18.671407":
    Возвращает строку с датой в формате: "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    # Отсечь и разделить дату
    date = date_time[:10]
    splitted_date = date.split('-')

    # Развенуть и склеить дату точками
    return '.'.join(splitted_date[::-1])
