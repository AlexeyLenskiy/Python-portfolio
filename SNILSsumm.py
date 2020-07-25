# importing random module
import random

print()
print("---------------------------SNILS GENERATOR v. 1.0---------------------------")
print()
print("Select programm mode by pressing 1, 2, 3 keys")
print("[1] - program generates valid SNILS number and counts SNILS control summ. ")
print("[2] - input first 9 number of SNILS. Programm counts SNILS control summ, control nuber and prints valid SNILS number")
print("[3] - input SNILS control number. Program generates valid SNILS number")
print("[4] - input SNILS control sum. Program generates valid SNILS number. **LONG CALCULATION TIME**")

numbers = '0123456789'

#generate random 9 SNILS numbers
def random_snils(numbers):
    rand_snils = ''
    for i in range(9):
        rand_snils += random.choice(numbers)
    return rand_snils

#inputing 9 numbers of SNILS without control number
def input_snils(inputs):

#validation checks for input data
    for n in range(len(inputs)):
        if inputs[n] not in '0123456789':
            print("SNILS must contain only numbers 0-9")
            break

        elif len(inputs) < 9:
            print("SNILS must be 9 numbers lenght")
            break

        else:
            return inputs

# defining controll summ count function (i1*9 + i2*8 +i3*7 + i4*6 + i5*5 + i6*4 + i7*3 + i8*2 +i9*1)
def snils_sum(snils):
    position = 10
    sum = 0
    for i in range(len(snils)):
        position -= 1
        count = position * int(snils[i])
        sum += count
    return sum

# defining SNILS control number by PF RF rules
def snils_control(snils_count):
    snils_count = snils_sum(snils)
    if snils_count <10:
        number = '0' + str(snils_count)
    if snils_count >= 10 and snils_count < 100:
        number = str(snils_count)
        return number
    elif snils_count == 100 or snils_count == 101:
        number = '00'
        return number
    else:
        number = str(snils_count % 101)
        return number

print("Select mode: ")
mode = input()

# mode 1 generate valid random SNILS number
if mode == '1':
    snils = random_snils(numbers)

    # counting SNILS control summ
    snils_count = snils_sum(snils)

    # counting SNILS control number
    snils_control_number = snils_control(snils_count)

    # defining SNILS number with control number
    SNILS = snils[0:3] + '-' + snils[3:6] + '-' + snils[6:9] + ' ' + snils_control_number

    # printing SNILS number and SNILS control sum
    print("SNILS number is: ", SNILS)
    print("SNILS control summ is: ", snils_count)

# mode 2
# input first 9 number of SNILS.
# program counts SNILS control sum, control number and print valid SNILS number
elif mode == '2':
    inputs = input("Enter number: ")
    snils = input_snils(inputs)

    # counting SNILS control summ
    snils_count = snils_sum(snils)

    # counting SNILS control number
    snils_control_number = snils_control(snils_count)

    # defining SNILS number with control number
    SNILS = snils[0:3] + '-' + snils[3:6] + '-' + snils[6:9] + ' ' + snils_control_number

    # printing SNILS number and SNILS control sum
    print("SNILS number is: ", SNILS)
    print("SNILS control summ is: ", snils_count)

elif mode == '3':
    input_num = input("Input control number: ")
    while True:

        snils = random_snils(numbers)

        # counting SNILS control summ
        snils_count = snils_sum(snils)

        # counting SNILS control number
        snils_control_number = snils_control(snils_count)
        if input_num == snils_control_number:

            # defining SNILS number with control number
            SNILS = snils[0:3] + '-' + snils[3:6] + '-' + snils[6:9] + ' ' + snils_control_number
            # printing SNILS number and SNILS control sum
            print("SNILS number is: ", SNILS)
            print("SNILS control summ is: ", snils_count)
            break

elif mode == '4':
    input_sum = input("Input control sum: ")
    while True:

        snils = random_snils(numbers)

        # counting SNILS control summ
        snils_count = snils_sum(snils)
        if input_sum == snils_count:

            # counting SNILS control number
            snils_control_number = snils_control(snils_count)

            # defining SNILS number with control number
            SNILS = snils[0:3] + '-' + snils[3:6] + '-' + snils[6:9] + ' ' + snils_control_number
            # printing SNILS number and SNILS control sum
            print("SNILS number is: ", SNILS)
            print("SNILS control summ is: ", snils_count)
            break






