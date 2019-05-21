#by Sony Yang

import random

def generate_password(password_size):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=:;"
    password = ""
    
    for num in range(password_size):
        chars_last_index = len(chars) - 1
        password += chars[random.randint(0, chars_last_index)]
        
    return password

def main():
    print(generate_password(8))


main()