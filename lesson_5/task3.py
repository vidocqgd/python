# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
# Решите через рекурсию. В задании нельзя применять циклы.


def calculation(n1, n2=0) -> int:
    n2 = n2 * 10 + n1 % 10
    n1 //= 10
    if n1 == 0:
        return n2
    return calculation(n1, n2)

num = int(input('Введите число: '))
z = calculation(num)
print(z)