"""
В изначальном примере было неправильное использование lambda. 
Предполагаю, что задумывалось, что в список handlers должны были быть добавлены callback-функции, которые создавались бы
при помощи lambda. 
Во-первых, из-за отсутствия в примере вызываемого объекта с именем callback код вообще не будет
работать.
Во-вторых, если бы такой объект присутствовал, то переменную step он бы как-то обрабатывал, 
получается, что lambda-функция возвращала лишь результат работы функции callback(). Можно было бы прописать логику
обработки функции callback() в lambda-функцию, например lambda: pow(step, 2) 
Но вообще, если речь идет о callback-функциях, то необходимости в lambda-функции (при наличии параметра callback) нет. 
"""


def create_handlers(callback: callable) -> list:
    handlers = [callback] * 5  # добавляем в список такое количество callback-функций, которое нам необходимо
    # handlers = [lambda num: pow(num, 2)]*5 тоже работает
    return handlers


def execute_handlers(handlers: list) -> list:
    # в изначальном варианте не было возвращения значения, добавил return
    return [handler(i) for i, handler in enumerate(handlers)]


# без return, тогда обработчик просто выполнит действие
def execute_handlers_1(handlers: list): # возвращаемого значения не будет
    for i, handler in enumerate(handlers):
        handler(i)


""""
Для примера будем считать, что callback-функция существует (называется callback_func). 
(Если бы не существовало), то в create_handlers вместо handlers=[callback]*5 можно было бы прописать 
handlers = [lambda num: pow(num, 2)]*5 - результат аналогичный

"""


def callback_func(num):  # callback-функция для примера
    return pow(num, 2)


callbacks = callback_func  # объявляем callback-функцию
handlers_list = create_handlers(callbacks)  # создаем переменную, которая хранит список обработчиков
print(execute_handlers(handlers_list))  # выводим результат работы обработчиков
execute_handlers_1(handlers_list)  # просто запускаем обработчики

"""
Ещё возможен такой вариант решения
"""


def create_handlers_2() -> list:  # убрать из параметров callback
    handlers = []
    for step in range(5):
        handlers.append(lambda step: step)  # добавляем callback функцию, которая просто принимает и возвращает значение
    return handlers


def execute_handlers_2(handlers: list) -> list:
    return [handler(i) for i, handler in enumerate(handlers)]
    # не вызываемый


handlers_list_2 = create_handlers_2()
print(execute_handlers_2(handlers_list_2))