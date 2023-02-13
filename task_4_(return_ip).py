# Написать функцию, которая возвращает публичный ip-адрес
import urllib.request


def get_ip() -> str:
    ip = urllib.request.urlopen('https://ifconfig.me/').read().decode('utf8')
    return ip


result_ip = get_ip()
print(result_ip)  # если необходим вывод только ip адреса

'''
Можно использовать такой вариант, если необходимо пояснение к выводимым данным:
print(f'Ваш ip-адрес: {result_ip}')
'''
