# KEYGEN V. 1.0

# Programm generate solid password with inputed lenght

import random

# entering password valid data
numbers = '1234567890'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
high_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '@#$%^&*()-+'

# define password lenght
while True:
    pass_l = int(input("Enter password lenght (12 symbols or more): "))
    if pass_l < 12:
        print("Solid password must be 12 or higher symbols lenght")
        break

# define pass generation function
    def pass_gen(numbers, low_letters, high_letters, symbols, pass_l):
        x_key = ''
        # generate 1 symbol of each data tipes
        x_key += random.choice(numbers)
        x_key += random.choice(low_letters)
        x_key += random.choice(high_letters)
        x_key += random.choice(symbols)

        # generate other symbols in password
        for i in range(pass_l - 4):
            pass_valids = numbers + low_letters + high_letters + symbols
            x_key += random.choice(pass_valids)
        # shuffle generated symbols in password
        pass_x = list(x_key)
        random.shuffle(pass_x)
        return ''.join(pass_x)

    # print generated password
    password = pass_gen(numbers, low_letters, high_letters, symbols, pass_l)
    print('Your password is: ', password)

    # Inspect how strong generated password
    for i in range(pass_l):
        pass_valids = numbers + low_letters + high_letters + symbols
        if password[i] not in pass_valids:
            err = 1
            break
        else:
            err = 0

    for i in range(len(high_letters)):
        if high_letters[i] in password:
            a = 1
            break
        else:
            a = 0

    for i in range(len(low_letters)):
        if low_letters[i] in password:
            b = 1
            break
        else:
            b = 0

    for i in range(len(numbers)):
        if numbers[i] in password:
            c = 1
            break
        else:
            c = 0

    for i in range(len(symbols)):
        if symbols[i] in password:
            d = 1
            break
        else:
            d = 0
    if err == 1:
        print("Error. Restricted symbol.")
    elif a + b + c + d == 4:
        print("Strong password.")
    elif a + b + c + d != 4:
        print("Weak password. Recomended: ", end='')
        if a == 0:
            print(f"add 1 upper letter", end=', ')
        if b == 0:
            print(f"add 1 lower letter", end=', ')
        if c == 0:
            print(f"add 1 digit", end=', ')
        if d == 0:
            print(f"add 1 special symbol", end='')

    # saving password in file
    print("Do you want to save password in file? y/n:")
    save = input()
    while True:
        if save == 'y':
            print("Enter file description")
            description = input() + ':  '
            openfile = open('PassList.txt', 'a')
            openfile.write(description)
            openfile.write(password)
            openfile.write('\n')
            openfile.close()
            break
        if save == 'n':
            print('Password not saved')
            break
        else:
            print("Chose 'y' or 'n'")
    break





