#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Время выполнения: {} секунд".format(end - start))
        return return_value
    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    wrapper = requests.get(url)
    return wrapper.text


if __name__ == '__main__':
    webpage = fetch_webpage('https://google.com')
    print(webpage)
