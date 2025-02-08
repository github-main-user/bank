from typing import Any

import pytest

from src.processing import filter_by_description, filter_by_state, sort_by_date

# Фикстуры


@pytest.fixture
def valid_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def invalid_data() -> list:
    return [123, "123", None]


# Фильтр


def test_valid_executed_filter(valid_data: list[dict]) -> None:
    assert filter_by_state(valid_data, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_valid_canceled_filter(valid_data: list[dict]) -> None:
    assert filter_by_state(valid_data, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize("state", ["asdfasbsf", "EXCUDT", "", 123, None])
def test_random_data_filter(valid_data: list[dict], state: Any) -> None:
    assert filter_by_state(valid_data, state) == []


@pytest.mark.parametrize("data", ["asdb", None, {}, 123])
def test_invalid_data_types_filter(data: Any) -> None:
    with pytest.raises(TypeError):
        filter_by_state(data)


def test_invalid_type_in_list_filter(invalid_data: list) -> None:
    with pytest.raises(TypeError):
        filter_by_state(invalid_data)


def test_filter_by_existing_pattern() -> None:
    operations = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            'description': 'Перевод организации',
        }
    ]
    assert filter_by_description(operations, 'перевод') == operations


def test_filter_by_non_existing_pattern() -> None:
    operations = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            'description': 'Перевод организации',
        }
    ]
    assert filter_by_description(operations, 'UwU') == []


# Сортировка


def test_valid_sort(valid_data: list[dict]) -> None:
    assert sort_by_date(valid_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_valid_sort_reverse(valid_data: list[dict]) -> None:
    assert sort_by_date(valid_data, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize("data", ["asdb", None, {}, 123])
def test_invalid_data_types_sort(data: list[Any]) -> None:
    with pytest.raises(TypeError):
        sort_by_date(data)


def test_invalid_type_in_list_sort(invalid_data: list[Any]) -> None:
    with pytest.raises(TypeError):
        sort_by_date(invalid_data)
