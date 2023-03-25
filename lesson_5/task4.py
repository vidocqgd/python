# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 0:
        return 1
    if B < 0:
        return 1 / power(A, -B)
    if B % 2 == 0:
        return power(A, B // 2) * power(A, B // 2)
    else:
        return power(A, B - 1) * A
    
A = int(input())
B = int(input())
print(power(A, B))