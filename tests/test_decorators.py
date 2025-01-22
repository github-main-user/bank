from typing import Any

import pytest

from src.decorators import log


@log(filename=None)
def add(a: int, b: int) -> int:
    return a + b


@log(filename=None)
def divide(a: int, b: int) -> float:
    return a / b


def test_log_success(capsys: Any) -> None:
    add(2, 3)

    captured = capsys.readouterr()
    assert "add ok\n" == captured.out


def test_log_error(capsys: Any) -> None:
    divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n" == captured.out
