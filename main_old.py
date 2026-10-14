try:
    name = input("Название товара: ")
    price = float(input("Цена: "))
    count = int(input("Количество: "))
except ValueError:
    print("Ошибка: введены некорректные данные")
    exit()

summa = price * count
if summa >= 15000:
    skidka = 15
elif summa >= 10000:
    skidka = 10
elif summa >= 5000:
    skidka = 5
else:
    skidka = 0
rub = summa * skidka / 100
itog = summa - rub
print("\nТовар:", name)
print("Цена:", price)
print("Количество:", count)
print("Итого:", summa)
print("Скидка в процентах:", skidka, "%")
print("Скидка в рублях:", rub)
print("Итоговая цена:", itog)