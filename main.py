import random

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = int(input("Количество паролей? " + "\n"))
lenght = int(input("Длинна пароля? " + "\n"))

for n in range(number):
    password = ""
    for i in range(lenght):
        password += random.choice(chars)
    print(password)
