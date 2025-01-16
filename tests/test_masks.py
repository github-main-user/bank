from typing import Any

import pytest

from src.masks import WrongNumberLengthError, get_mask_account, get_mask_card_number


# Фикстуры
@pytest.fixture
def invalid_card_number_length() -> int:
    return 1234567890123  # 13 цифр


@pytest.fixture
def invalid_account_number_length() -> int:
    return 123456789012345674412624192  # 27 цифр


@pytest.fixture
def invalid_data_type() -> str:
    return "invalid"


# Тесты карты
@pytest.mark.parametrize(
    "card_number,expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (9876543210987654, "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number_success(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_length(invalid_card_number_length: int) -> None:
    with pytest.raises(WrongNumberLengthError):
        get_mask_card_number(invalid_card_number_length)


def test_get_mask_card_number_invalid_type(invalid_data_type: Any) -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_data_type)


# Тесты счёта
@pytest.mark.parametrize(
    "account_number,expected",
    [
        (12345678901234567890, "**7890"),
        (98765432109876543210, "**3210"),
    ],
)
def test_get_mask_account_success(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_length(invalid_account_number_length: int) -> None:
    with pytest.raises(WrongNumberLengthError):
        get_mask_account(invalid_account_number_length)


def test_get_mask_account_invalid_type(invalid_data_type: Any) -> None:
    with pytest.raises(TypeError):
        get_mask_account(invalid_data_type)
