
# Задание 2.

# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

my_list = [b'class', b'function', b'method']

for line in my_list:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной: {}\n'.format(line))
    print('Длина переменной: {}\n'.format(len(line)))