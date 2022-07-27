print("***Password Generator****")
import random
import string

caracters = string.printable

def get_password():
    password_length = int(input('\n'"Enter the length of the password :"))
    return "".join(random.sample(caracters,password_length))

print(get_password())



