#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
import os
os.system("cls")
print("Введите число: ")
a = int(input())
print("Введите степень: ")
b = int(input())
def func(a, b):
    if b == 0:
        return 1
    return a * func(a, b - 1)
print(f"Ответ: {a} в {b} степени = {func(a, b)}")
input("PRESS ENTER")