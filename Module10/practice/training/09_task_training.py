# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random
import random

def f2(n, a, b):
    return [random.randint(a, b) for _ in range(n)]
