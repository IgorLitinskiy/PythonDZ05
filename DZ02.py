#Задача 28: Напишите рекурсивную функцию sum(a, b),возвращающую сумму двух целых неотрицательных чисел.
#Из всех арифметических операций допускаются только +1 и -1.Также нельзя использовать циклы.
import os
os.system("CLS")
print("Введите первое неотрицительное число: ")
a = int(input())
print("Введите второе неотрицательно число: ")
b = int(input())
def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)
print(f"Ответ: {recursive_sum(a, b)}")
input("PRESS ENTER")