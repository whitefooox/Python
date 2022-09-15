def check_password(func):
    flag = True
    def wrapper(n):
        nonlocal flag
        if flag:
            if input('Пароль: ') != '123':
                print("В доступе отказано")
                return None
            else:
                flag = False
                return func(n)
    return wrapper

@check_password
def fibonacci(n):
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return f2

print(fibonacci(10))