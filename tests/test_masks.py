from src.masks import get_mask_card_number, get_mask_account, WrongNumberLengthError
import pytest


@pytest.mark.parametrize(
    'card, mask',
    [
        (7000792289606361, '7000 79** **** 6361'),
        (1234567812345670, '1234 56** **** 5670'),
        (9876543210987654, '9876 54** **** 7654'),
        (4000123412341234, '4000 12** **** 1234'),
        (5555444433332222, '5555 44** **** 2222'),
    ],
)
def test_mask_card_numbers(card, mask):
    assert get_mask_card_number(card) == mask


@pytest.mark.parametrize(
    'card',
    [7020079228960636241, 972134, 0],
)
def test_mask_card_number_wrong_length(card):
    with pytest.raises(WrongNumberLengthError):
        get_mask_card_number(card)
