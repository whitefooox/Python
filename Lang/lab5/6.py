last_message = ''

def print_without_duplicates(message):
    global last_message
    if message != last_message:
        print(message)
    last_message = message

n = int(input())

for _ in range(n):
    print_without_duplicates(input())