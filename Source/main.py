from random import randint
from config import *
from oneNumberExpressions import one_number_menu
from logo import get_logo


def start():
    cls()
    print("Приветствую вас в своем помощнике старшеклассника! В нем вы найдете многое, что понадобится вам в учебе!")
    input("Для продолжения нажмите клавишу enter...")


def bye():
    cls()
    print("Спасибо, что воспользовались моим помощником!")
    print(get_logo())
    input("Для выхода нажмите клавишу enter...")


def basic_calculator():
    expression = input('Введите пример:\n')
    print(f'{expression} = {eval(expression)}')
    input("Для продолжения нажмите клавишу enter...")


def menu():
    cls()
    print("Меню:")
    choose = 0
    for i in range(len(menuConfig)):
        print(f"{i + 1}. {menuConfig[i]}")
    try:
        choose = int(input("Ваш выбор: "))
    except Exception as _ex:
        print(f'Неверный ввод. ({_ex})')
        menu()
    if choose == 1:
        one_number_menu()
        menu()
    elif choose == 2:
        basic_calculator()
        menu()
    elif choose == len(menuConfig):
        return
    else:
        menu()


def main():
    start()
    menu()
    bye()

if __name__ == "__main__":
    main()