import pytest

from src.masks import WrongNumberLengthError
from src.widget import InvalidFormatError, get_date, mask_account_card


# Фикстуры
@pytest.fixture
def wrong_number_length_card() -> str:
    return "Visa Platinum 129384"


@pytest.fixture
def wrong_number_length_account() -> str:
    return "Счёт 120938471029385761029387410293874109237"


@pytest.fixture
def empty_card_info() -> str:
    return "1234098712536295"


@pytest.fixture
def empty_card_number() -> str:
    return "Visa Platinum"


@pytest.fixture
def invalid_date_string() -> str:
    return "2024-03"


# Карты
@pytest.mark.parametrize(
    "card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("MasterCard 7123792289607712", "MasterCard 7123 79** **** 7712"),
    ],
)
def test_valid_cards(card: str, expected: str):
    assert mask_account_card(card) == expected


def test_wrong_number_length_card(wrong_number_length_card: str):
    with pytest.raises(WrongNumberLengthError):
        mask_account_card(wrong_number_length_card)


def test_empty_card_info(empty_card_info: str):
    with pytest.raises(InvalidFormatError):
        mask_account_card(empty_card_info)


def test_empty_card_number(empty_card_number: str):
    with pytest.raises(InvalidFormatError):
        mask_account_card(empty_card_number)


# Счета
@pytest.mark.parametrize(
    "account, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12093847123568120938", "Счет **0938"),
        ("Счет 12093874129386555551", "Счет **5551"),
    ],
)
def test_valid_accounts(account: str, expected: str):
    assert mask_account_card(account) == expected


def test_wrong_number_length_account(wrong_number_length_account: str):
    with pytest.raises(WrongNumberLengthError):
        mask_account_card(wrong_number_length_account)


@pytest.mark.parametrize("data", [{}, None, 234])
def test_invalid_data_type_mask(data):
    with pytest.raises(TypeError):
        mask_account_card(data)


# Дата
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1997-11-01T02:06:18.123442", "01.11.1997"),
        ("2003-07-06T02:26:18.671407", "06.07.2003"),
    ],
)
def test_date(date: str, expected: str):
    assert get_date(date) == expected


def test_invalid_date(invalid_date_string: str):
    with pytest.raises(InvalidFormatError):
        get_date(invalid_date_string)


@pytest.mark.parametrize("data", [{}, None, 234])
def test_invalid_data_type_date(data):
    with pytest.raises(TypeError):
        get_date(data)
