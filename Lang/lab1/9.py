ok = False

while ok != True:
    password1 = input()
    password2 = input()
    if len(password1) < 8:
        print("Короткий!")
    elif "123" in password1:
        print("Простой!")
    elif password1 != password2:
        print("Различаются.")
    else:
        ok = True

print("ОК")
