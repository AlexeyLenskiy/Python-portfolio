

#inputing 9 numbers of SNILS without control number
snils = input("Enter number: ")

#validation checks for input data
for n in range(len(snils)):
    if snils[n] not in '0123456789':
        print("SNILS must contain only numbers 0-9")
        break

    elif len(snils) < 9:
        print("SNILS must be 9 numbers lenght")
        break

    else:
#defining controll summ count function (i1*9 + i2*8 +i3*7 + i4*6 + i5*5 + i6*4 + i7*3 + i8*2 +i9*1)
        def snils_sum(snils):
            position = 10
            sum = 0
            for i in range(len(snils)):
                position -= 1
                count = position * int(snils[i])
                sum += count
            return sum

        snils_control = snils_sum(snils)

#printing SNILS control summ
        print("SNILS control summ is: ", snils_control)

#defining SNILS control number by PF RF rules
        if snils_control < 100:
                number = snils_control
        elif snils_control == 100 or snils_control == 101:
                number = 00
        else:
            number = snils_control % 101

        if number < 10:
            number = '0' + str(number)
        else:
            number = str(number)

#printing SNILS control number
        print("SNILS control number is: ", number)

#defining SNILS number with control number
        SNILS = snils[0:3] + '-' + snils [3:6] + '-' + snils[6:9] + ' ' + number

#printing SNILS number with control number
        print("SNILS number is: ", SNILS)
        break