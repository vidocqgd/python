# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
arr = []
for i in range(20):
	x = int(random.random()*10)  
	arr.append(x)
	print("%3d" % x, end='')
	if (i+1) % 10 == 0:	print()
 
minimum = int(input('min: '))
maximum = int(input('max: '))
 
index = []
i = 0
for i in arr:
	if minimum <= i <= maximum:
		index.append(arr.index(i))
print("Количество: ", len(index))
print("Индексы: ", index)
b=[]
while i < len(arr):
    if 0 <= i <= 3:
        b.append(arr[i])
        del arr[i]
    else:    
        i += 1
print(b)
print("Обновлённый список", arr)	