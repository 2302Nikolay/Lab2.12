#!/usr/bin/env python3

def decorator_with_name(name):
    print('>decorator_with_name: ', name)

    def real_decorator(func):
        print('>>Сам декоратор: ', func.__name__)

        def decorated(*args, **kwargs):
            print('>>> Перед функц ', func.__name__)
            ret = func(*args, **kwargs)
            print('>>> После функциис', func.__name__)
            return ret
        return decorated
    return real_decorator


@decorator_with_name('test')
def add(a, b):
    print(" >>>> Функция add")
    return a + b


print("Старт программы")
r = add(10, 10)
print(r)
print("Конец программы")
