login = input()
email = input()

if "@" not in login and "@" in email:
    print("верно")
else:
    print("не верно")
