# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, введено число 3. Считаем 3 + 33 + 333 = 369.

number = input("Enter number: ")
a = int(number + number)
b = int(number+number+number)
summa = int(number) + a + b

print(summa)