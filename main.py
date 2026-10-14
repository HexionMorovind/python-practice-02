# -*- coding: utf-8 -*-
"""
Практическая работа №2 (Вариант 4).
Расчёт стоимости покупки: несколько товаров, скидка 5% при подытоге > 5000.
"""

DISCOUNT_THRESHOLD = 5000.0
DISCOUNT_RATE = 0.05


def ask_yes_no(prompt: str) -> bool:
    """Запрашивает ответ да/нет, повторяет при некорректном вводе."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Ошибка: введите 'да' или 'нет'.")


def ask_positive_float(prompt: str) -> float:
    """Запрашивает положительное число, повторяет при ошибке."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Ошибка: введите корректное число.")
            continue
        if value <= 0:
            print("Ошибка: значение должно быть положительным.")
            continue
        return value


def ask_positive_int(prompt: str) -> int:
    """Запрашивает положительное целое число."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value <= 0:
            print("Ошибка: значение должно быть положительным.")
            continue
        return value


def ask_non_empty(prompt: str) -> str:
    """Запрашивает непустую строку."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: название не должно быть пустым.")


def input_item() -> dict:
    """Ввод одного товара с проверками."""
    name = ask_non_empty("Введите название товара: ")
    price = ask_positive_float("Введите цену: ")
    quantity = ask_positive_int("Введите количество: ")
    return {"name": name, "price": price, "quantity": quantity}


def calculate_total(items: list) -> tuple:
    """Возвращает (подытог, скидка, итог)."""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0.0
    total = subtotal - discount
    return subtotal, discount, total


def print_receipt(items: list, subtotal: float, discount: float, total: float) -> None:
    print("\n=== Чек ===")
    for item in items:
        line_sum = item["price"] * item["quantity"]
        print(f"{item['name']}: {item['price']:.2f} x {item['quantity']} = {line_sum:.2f}")
    print("-" * 30)
    print(f"Подытог: {subtotal:.2f}")
    if discount > 0:
        print(f"Скидка 5%: -{discount:.2f}")
    print(f"Итого к оплате: {total:.2f}")


def main() -> None:
    print("=== Расчёт стоимости покупки ===")
    items = []

    while True:
        item = input_item()
        items.append(item)
        if not ask_yes_no("Добавить ещё один товар? (да/нет): "):
            break

    subtotal, discount, total = calculate_total(items)
    print_receipt(items, subtotal, discount, total)
    print("\nРабота программы завершена.")


if __name__ == "__main__":
    main()