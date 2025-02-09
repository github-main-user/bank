from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.transactions_pandas import load_transactions_csv, load_transactions_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

FILE_TYPES = ["JSON", "CSV", "XLSX"]
FILTER_STATUSES = ["EXECUTED", "CANCELED", "PENDING"]
YES_NO_CHOICES = ["Да", "Нет"]
PROMPT = "> "


def ask_user_for_choice(choices: list[str], wrong_input_msg: str = 'Ввод "{}" не принят') -> str:
    while True:
        user_choise = str(input(PROMPT))
        if user_choise.lower() in map(str.lower, choices):
            return user_choise
        print(wrong_input_msg.format(user_choise))


def main() -> None:
    # -- ПРИВЕТСТВИЕ И ВОПРОСЫ --
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    for i, file_type in enumerate(FILE_TYPES, start=1):
        print(f"{i}. Получить информацию о транзакциях из {file_type}-файла")

    # Запрашиваем тип файла у пользователя
    index_choices = list(map(str, range(1, len(FILE_TYPES) + 1)))
    index = int(ask_user_for_choice(index_choices)) - 1
    chosen_file_type = FILE_TYPES[index]
    print(f"Для обработки выбран {chosen_file_type}-файл.")

    # Запрашиваем статус для фильтрации у пользователя
    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    print(f"Доступные для фильтрации статусы: {', '.join(FILTER_STATUSES)}")
    chosen_filter_status = ask_user_for_choice(FILTER_STATUSES, 'Статус операции "{}" недоступен.').upper()

    print(f"\nОтсортировать операции по дате? {'/'.join(YES_NO_CHOICES)}")
    filter_by_date = True if ask_user_for_choice(YES_NO_CHOICES).lower() == "да" else False

    sort_order = "по убыванию"
    if filter_by_date:
        print("\nОтсортировать по возрастанию или по убыванию?")
        sort_order = ask_user_for_choice(["по возрастанию", "по убыванию"])

    print(f"\nВыводить только рублёвые транзакции? {'/'.join(YES_NO_CHOICES)}")
    show_only_rub = True if ask_user_for_choice(YES_NO_CHOICES).lower() == "да" else False

    print(f"\nОтфильтровать список транзакций по определённому слову в описании? {'/'.join(YES_NO_CHOICES)}")
    filter_by_word = True if ask_user_for_choice(YES_NO_CHOICES).lower() == "да" else False
    filter_pattern = ""
    if filter_by_word:
        print("\nВведите слово для фильтрации")
        filter_pattern = input(PROMPT)

    # -- РАСЧЁТ --
    file_type_to_load_function_map = {
        "JSON": load_transactions("data/operations.json"),
        "CSV": load_transactions_csv("data/transactions.csv"),
        "XLSX": load_transactions_excel("data/transactions_excel.xlsx"),
    }
    transactions = file_type_to_load_function_map[chosen_file_type]

    transactions = filter_by_state(transactions, chosen_filter_status)

    if filter_by_date:
        transactions = sort_by_date(transactions, reverse=sort_order == "по убыванию")

    if show_only_rub:
        transactions = list(filter_by_currency(transactions, "RUB"))

    if filter_by_word:
        transactions = filter_by_description(transactions, filter_pattern)

    # -- ИТОГ --
    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        date = get_date(transaction["date"])
        description = transaction["description"]
        print(f"\n{date} {description}")

        from_ = transaction.get("from")
        if from_:
            print(mask_account_card(from_), "->", end=" ")
        print(mask_account_card(transaction["to"]))

        operation_amount = transaction.get("operationAmount", {})
        amount = operation_amount.get("amount")
        currency = operation_amount.get("currency", {}).get("name")
        if amount and currency:
            print(f"Сумма: {amount} {currency}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Завершение программы")
