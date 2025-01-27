from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: Если задано, логи записываются в файл, иначе выводятся в консоль.
    """

    def decorator(func: Callable) -> Callable:
        func_name = func.__name__

        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)

                # my_function ok
                log_message = f"{func_name} ok"

                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

                return result
            except Exception as e:
                # my_function error: тип ошибки. Inputs: (1, 2), {}
                log_message = f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

        return inner

    return decorator
