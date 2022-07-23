from config import oneNumberExpressionsConfig, cls
from math import log


def one_number_menu():
    print("Выберите действие:")
    choose = 0
    for i in range(len(oneNumberExpressionsConfig)):
        print(f"{i + 1}. {oneNumberExpressionsConfig[i]}")
    try:
        choose = int(input("Ваш выбор: "))
    except Exception as _ex:
        print(f'Неверный ввод. ({_ex})')
        one_number_menu()
    if choose == 1:
        cls()
        value = float(input("Введите число: "))
        print(sqrt(value))
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 2:
        cls()
        value = float(input("Введите число: "))
        degree = float(input("Введите степень: "))
        print(raise_to_degree(value, degree))
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 3:
        cls()
        value = int(input("Введите целое число: "))
        print(factorial(value))
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 4:
        cls()
        value = int(input("Введите целое число: "))
        result = "Простое" if is_prime(value) else "Не простое"
        print(result)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 5:
        cls()
        print("Логарифм натуральный?\n1. Да\n2. Нет")
        is_natural = True if int(input("Ваш выбор: ")) == 1 else False
        value = int(input("Введите целое число: "))
        if is_natural:
            print(log(value))
        else:
            base = int(input("Введите целое основание: "))
            print(log(value, base))
        input("Для продолжения нажмите клавишу enter...")
    else:
        pass


def factorial(value):
    fact = 1
    for i in range(1, value+1):
        fact = fact * i
    return fact


def raise_to_degree(value, degree):
    return value**degree


def sqrt(value):
    return raise_to_degree(value, 0.5)


def is_prime(value):
    count = 0
    i = 2
    while i < value/2:
        if value % i == 0:
            count += 1
        i += 1
    if count > 0:
        return False
    return True
