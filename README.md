# Описание
В проекте реализованы модули для работы с виджетом банковских операций клиента.
Для взаимодействия используется файл `main.py`.

# Функциональность
В модуле `src/widget.py` реализованы 2 функции:
1. `mask_account_card` - позволяет скрыть номер карты/счёта, использует соответствующие функции из модуля `src/masks.py`.
2. `get_date` - позволяет получить дату из строки вида "2024-03-11T02:26:18.671407".

В модуле `src/processing.py` реализованы 3 функции для обработки банковских операций:
1. `filter_by_state` - фильтрует операции по переданному параметру `state`.
2. `sort_by_date` - возвращает новый отсортированный список операций.
3. `filter_by_description` - фильтрует операции по переданному шаблону, использует regex для поиска.
4. `count_operation_by_category` - подсчитывает категории в переданных операциях, возвращает словарь `{'категория': <количество_раз>}`

В модуле `src/generators.py` реализовано 3 генератора:
1. `filter_by_currency` - фильтрует транзакции по коду валюты, возвращает по 1й транзакции.
2. `transaction_descriptions` - возвращает описание транзакции.
3. `card_number_generator` - генерирует номера карт в заданном диапазоне, используя шаблон "XXXX XXXX XXXX XXXX".

В модуле `src/decorators.py` реализован декоратор `log`:
Пример использования декоратора:
```python
@log(filename="mylog.txt")
def divide(x, y):
    return x / y

divide(1, 2)
```

Ожидаемый вывод в лог-файл `mylog.txt` при успешном выполнении:
```text
divide ok
```

Ожидаемый вывод при ошибке:
```python
devide(1, 0)
```
```text
divide error: ZeroDivisionError. Inputs: (1, 0), {}
```

В модуле `src/utils.py` реализовано 2 функции:
1. `load_transactions` - Загружает данные о финансовых транзакциях из переданного JSON-файла.
2. `get_transaction_amount_rub` - Возвращает сумму транзакции в рублях, если необходимо, конвертирует иную валюту в рубли.

В модуле `src/transactions_pandas.py` реализовано 2 функции использующие pandas:
1. `load_transactions_csv` - Загружает данные о финансовых транзакциях из переданного csv-файла используя pandas.
2. `load_transactions_excel` - Загружает данные о финансовых транзакциях из переданного excel-файла используя pandas.

# Тесты
Модули обеспечены тестами в папке `tests`.

Запуск тестов происходит через `pytest`:
```shell
pytest
```
Для того чтобы проверить покрытие тестами:
```shell
pytest --cov src
```

# Установка

1. Склонировать репозиторий:
```shell
git clone https://github.com/github-main-user/bank.git
```
или
```shell
git clone git@github.com:github-main-user/bank.git
```

2. Зайти в директорию с проектом:
```shell
cd bank
```

3. Создать виртуальное окружение и установить необходимые зависимости:
```shell
poetry install
```

4. Запуск программы:
```shell
python main.py
```
