from unittest.mock import Mock, patch

import pytest

from src.transactions_pandas import load_transactions_csv, load_transactions_excel


@patch("pandas.read_csv")
def test_load_transactions_csv(mock_read_csv) -> None:
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 2000}]
    mock_read_csv.return_value = mock_df
    assert load_transactions_csv("fake.csv") == [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 2000}]


@patch("pandas.read_excel")
def test_load_transactions_excel(mock_read_excel) -> None:
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 2000}]
    mock_read_excel.return_value = mock_df
    assert load_transactions_excel("fake.xlsx") == [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 2000}]


def test_load_transactionos_csv_wrong_file() -> None:
    with pytest.raises(FileNotFoundError):
        load_transactions_csv("WRONG_PATH")


def test_load_transactionos_excel_wrong_file() -> None:
    with pytest.raises(FileNotFoundError):
        load_transactions_excel("WRONG_PATH")
