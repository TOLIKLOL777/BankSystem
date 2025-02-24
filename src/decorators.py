from functools import wraps


def log(filename=""):
    """Проверяет функцию на ошибки
    и если в начале дано название файла то записывает лог в файл если нет то выводит в консоль"""

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename == "":
                    return f"{func.__name__} error:{type(e).__name__}. Inputs: {args}, {kwargs}"
                else:
                    log_file = open(filename, "w")
                    log_file.write(f"{func.__name__} error:{type(e).__name__}. Inputs: {args}, {kwargs}")
                    log_file.close()
            else:
                if filename == "":
                    return func.__name__ + " ok"
                else:
                    log_file = open(filename, "w")
                    log_file.write(func.__name__ + " ok")
                    log_file.close()
            return ""

        return inner

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 3))
