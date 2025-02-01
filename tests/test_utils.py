from unittest.mock import Mock, mock_open, patch

import pytest

from src.utils import _get_exchange_rate_to_rub, get_transaction_amount_rub, load_transactions

# Тест load_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
@patch("os.path.exists", return_value=True)
def test_load_transactions_valid_json(mock_exists, mock_file) -> None:
    transactions = load_transactions("dummy_path.json")
    assert len(transactions) == 1
    assert transactions[0]["amount"] == 100
    assert transactions[0]["currency"] == "USD"


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
@patch("os.path.exists", return_value=True)
def test_load_transactions_invalid_json_not_list(mock_exists, mock_file) -> None:
    transactions = load_transactions("dummy_path.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
@patch("os.path.exists", return_value=True)
def test_load_transactions_invalid_json_format(mock_exists, mock_file) -> None:
    transactions = load_transactions("dummy_path.json")
    assert transactions == []


@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found(mock_exists) -> None:
    transactions = load_transactions("non_existent.json")
    assert transactions == []


# Тест get_transaction_amount_rub


@patch("src.utils.requests.get")
def test_get_exchange_rate_to_rub(mock_get) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = mock_response

    exchange_rate = _get_exchange_rate_to_rub("USD")
    assert exchange_rate == 75.0

    exchange_rate = _get_exchange_rate_to_rub("RUB")
    assert exchange_rate == 1.0


@patch("src.utils.requests.get")
def test_get_exchange_rate_to_rub_bad_request(mock_get) -> None:
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Error with API: Bad Request"):
        _get_exchange_rate_to_rub("EUR")


@patch("src.utils._get_exchange_rate_to_rub")
def test_get_transaction_amount_rub(mock_exchange_rate) -> None:
    mock_exchange_rate.return_value = 75.0
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    result = get_transaction_amount_rub(transaction)
    assert result == 7500.0


def test_get_transaction_amount_wront_input() -> None:
    assert get_transaction_amount_rub({}) == 0
    assert get_transaction_amount_rub({"operationAmount": {}}) == 0
    assert get_transaction_amount_rub({"operationAmount": {"amount": "abc"}}) == 0
