#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""""
Объявите функцию с именем get_sq , которая вычисляет площадь прямоугольника по двум
параметрам: width и height – ширина и высота прямоугольника и возвращает результат.
Определите декоратор для этой функции с именем (внешней функции) func_show , который
отображает результат на экране в виде строки (без кавычек): "Площадь прямоугольника:
<значение>". Вызовите декорированную функцию get_sq .
"""""


def func_show(func):
    def wrapper(*args):
        rw = 1
        for i in args:
            rw *= i
        print(f"Площадь прямоугольника: ", func(*args))
        return func(*args)

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


if __name__ == '__main__':
    w = int(input("Введите ширину: "))
    h = int(input("Введите высоту: "))
    get_sq(w, h)
