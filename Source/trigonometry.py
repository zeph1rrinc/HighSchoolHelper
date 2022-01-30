from config import trigonometryConfig, anglesConfig, PI
from math import sin, cos, tan, degrees, radians


def trigonometry_menu():
    print("Выберите действие:")
    choose = 0
    for i in range(len(trigonometryConfig)):
        print(f"{i + 1}. {trigonometryConfig[i]}")
    try:
        choose = int(input("Ваш выбор: "))
    except Exception as _ex:
        print(f'Неверный ввод. ({_ex})')
        trigonometry_menu()
    if choose == 1:
        angle = int(input("Введите угол в градусах: "))
        sinus = anglesConfig[str(angle)]["sin"] if str(angle) in anglesConfig else sin(radians(angle))
        print(sinus)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 2:
        angle = int(input("Введите угол в градусах: "))
        cosinus = anglesConfig[str(angle)]["cos"] if str(angle) in anglesConfig else cos(radians(angle))
        print(cosinus)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 3:
        angle = int(input("Введите угол в градусах: "))
        tangens = anglesConfig[str(angle)]["tan"] if str(angle) in anglesConfig else tan(radians(angle))
        print(tangens)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 4:
        angle = int(input("Введите угол в градусах: "))
        cotangens = anglesConfig[str(angle)]["cot"] if str(angle) in anglesConfig else 1/tan(radians(angle))
        print(cotangens)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 5:
        angle = input("Введите угол в формате (3p/2): ")
        result = convert(angle)
        if result:
            print(f'{angle} = {int(round(result))}')
        else:
            print("Неверный ввод")
        input("Для продолжения нажмите клавишу enter...")
    elif choose == 6:
        angle = int(input("Введите угол: "))
        result = anglesConfig[str(angle)]["rad"] if str(angle) in anglesConfig else round(radians(angle), 3)
        print(result)
        input("Для продолжения нажмите клавишу enter...")
    elif choose == len(trigonometryConfig):
        return



def convert(angle):
    result = float(1)
    is_numerator = True
    for i in angle:
        if i.isdigit():
            if is_numerator:
                result *= int(i)
            else:
                result /= int(i)
        elif i == "p":
            if is_numerator:
                result *= PI
            else:
                result /= PI
        elif i == "/":
            if is_numerator:
                is_numerator = False
        else:
            return False
    return degrees(result)
