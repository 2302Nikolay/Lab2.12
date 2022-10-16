#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def hello_world():
    print("Hello, world!")


def higher_order(func):
    print("Получена функция {} в качестве аргумента".format(func))
    func()
    return func


if __name__ == '__main__':
    higher_order(hello_world)
