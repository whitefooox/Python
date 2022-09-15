with open('res/image.bmp', 'rb') as input_file:
    temp = bytes(input_file.read())

negativ = []
for i, elem in enumerate(temp):
    if i < 54:
        negativ.append(elem)
    else:
        negativ.append(255 - elem)

with open('res/output.bmp', 'wb') as output_file:
    output_file.write(bytes(negativ))