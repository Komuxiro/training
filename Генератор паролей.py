import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# укажем колличество паролей и длину паролей которые хочет получить пользователь
number = int(input('количество паролей?' + "\n"))
length = int(input('длина пароля?' + "\n"))
# цикл для генерации пароля
for n in range(number):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)
