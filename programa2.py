import _random

caracteres =   "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("ingresa la longitud de tu contraseña"))
password =""

for i in range(longitud):
    password += random.choice(caracteres)

print(password)
