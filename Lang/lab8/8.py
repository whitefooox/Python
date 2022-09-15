def reverse():
    with open('res/input.dat', 'rb') as input_file:
        temp = input_file.read()
    with open('res/output.dat', 'wb') as out_file:
        out_file.write(temp[::-1])

reverse()