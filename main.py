
"""
Практическая работа №2 (Вариант 4).
Расчёт стоимости покупки: несколько товаров подряд.
Скидка: >= 15000 -> 15%, >= 10000 -> 10%, >= 5000 -> 5%.
"""

items = []

while True:
    try:
        name = input("Название товара: ")
        price = float(input("Цена: "))
        count = int(input("Количество: "))
    except ValueError:
        print("Ошибка: введены некорректные данные")
        continue

    if not name.strip():
        print("Ошибка: название товара не должно быть пустым")
        continue
    if price <= 0 or count <= 0:
        print("Ошибка: цена и количество должны быть положительными")
        continue

    items.append((name, price, count))

    answer = input("Добавить ещё один товар? (да/нет): ").strip().lower()
    if answer == "нет":
        break
    elif answer != "да":
        print("Ошибка: введите 'да' или 'нет'. Считаем, что вы ответили 'да'.")

print("\n=== Чек ===")
total = 0
for name, price, count in items:
    summa = price * count
    total += summa
    print(f"{name}: {price} x {count} = {summa}")

if total >= 15000:
    skidka = 15
elif total >= 10000:
    skidka = 10
elif total >= 5000:
    skidka = 5
else:
    skidka = 0

rub = total * skidka / 100
itog = total - rub

print("\nСумма без скидки:", total)
print("Скидка в процентах:", skidka, "%")
print("Скидка в рублях:", rub)
print("Итоговая цена:", itog)