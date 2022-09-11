from datetime import datetime
import os
import sys
def path_log(path_):
    def decor(calculator):
        def calculator_log(*args, **kwargs):
            with open('log_file.txt', 'a', encoding="utf-8") as f:
                f.write(f'{datetime.now()} из файла {path_} вызвана функция {calculator.__name__} c аргументами {args} и {kwargs}')
                result = calculator(*args, **kwargs)
            with open('log_file.txt', 'a', encoding="utf-8") as f:
                f.write(f'и результатом {result}\n')
            return result
        return calculator_log
    return decor




