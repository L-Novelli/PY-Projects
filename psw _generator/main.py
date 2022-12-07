import random
import time
print('WELCOME TO PASSWORD GENERATOR!')
time.sleep(0.5)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().-_0123456789'

number = int(input("How many passwords do you want to generate?: \t"))
time.sleep(0.5)

length = int(input("Lenght of the password?: \t\t\t"))
time.sleep(0.5)

print("Here are your passwords:")

for psw in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(f'\t{password}')
    