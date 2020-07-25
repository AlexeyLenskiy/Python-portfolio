# program open txt.file with personal data table
# create e-mail for each person
# generate strong password for each person
# clear invalid data from "task_file.txt" and write to "invalid_data.txt"
# add e-mails and passwords in table
# write new data table in file "data_table.txt"


# import random moduls for password generator
import random

# import re modul for search and clearing invalid data
import re

# get data from file 'task_file.txt'
openfile = open('task_file.txt')
data = str(openfile.read())

# add PASSWORD column to data description
data_descr = 'NAME, LAST_NAME, TEL, CITY, PASSWORD'

                            # transform data for operations in programm #
########################################################################################
# transform data to list
data_1 = data.split('\n, ')

# transform invalid data strings to empty strings
for n in range(len(data_1)):
    # remove '\n' from data_1
    data_1[n] = re.sub(r'\n', '', data_1[n])
    # remove empty strings from data_1
    if re.findall(r', ,', data_1[n]):
        data_1[n] = ''
    # remove invalid data formats from data_1
    elif re.findall(r'[A-Z][a-z]+\, [A-Z][a-z]+\, \d+\, [A-Z][a-z]+', data_1[n]):
        data_1[n] = data_1[n]
    else:
        data_1[n] = ''
    # remove phones != 7 numbers from data_1
    if re.findall(r'[A-Z][a-z]+\, [A-Z][a-z]+\, \d{7}\, [A-Z][a-z]+', data_1[n]):
        data_1[n] = data_1[n]
    else:
        data_1[n] = ''


# clear invalid data in data_1
clear_data = []
for n in range(len(data_1)):
    if data_1[n] != '':
        clear_data += [data_1[n]]
    else:
        delete_string = data_1[n]
        del delete_string


# define inputs for email gen
def inputs(x):
    row = str(clear_data[x])
    row = row.split(', ')
    return [[row[0], row[1]]]

# define list of names for email gen
list_of_names = []
for x in range(len(clear_data)):
    list_of_names += inputs(x)


                            # email generator #
##########################################################################
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0] + str(letter) + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

# create name, surname, phone, adres in rows
def personal_data_row(x):
    row = str(clear_data[x])
    row = row.split(', ')
    return str(row[0]) + ', ' + str(row[1]) + ', ' + str(row[2]) + ', ' + str(row[3])

# create email row
def email_row(x):
    column_mail = str(email_gen(list_of_names)[x])
    return column_mail


                       # password generator #
####################################################################################
# Program generate solid password in 15 symbols

# entering password valid symbols
numbers = '1234567890'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
high_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '@#$%^&*()-+'

# define password lenght
pass_l = 15

# define pass generation function
def pass_gen(numbers, low_letters, high_letters, symbols, pass_l):
    x_key = ''
    # generate 1 symbol of each data types for strong password
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

# define generated password
password = pass_gen(numbers, low_letters, high_letters, symbols, pass_l)

# create password row
def password_row(x):
    column_password = str(pass_gen(numbers, low_letters, high_letters, symbols, pass_l))
    return column_password


                    # create new data table with emails and passwords#
#################################################################################
# define new data row
def new_data_row(x):
    row = str(clear_data[x])
    row = row.split(', ')
    # define valid data
    if row[0] and row[1] and row[2] and row[3] != ' ' and len(row[2]) == 7 and row[2].isnumeric():
        new_row = email_row(x) + ', ' + personal_data_row(x) + ', ' + password_row(x)
    # put invalid data row in table as empty row
    else:
        new_row = ''
    return new_row

# transform new data in table
new_data = ''
invalid_personal_data = ''
for x in range(len(clear_data)):
    newdata_row = new_data_row(x)
    # delete invalid data row from table
    if new_data_row(x) == '':
        invalid_personal_data += str(personal_data_row(x)) + '\n'
        del newdata_row
    # format valid data as string rows
    else:
        new_data += new_data_row(x) + '\n'

# add description row to data table
new_data = data_descr + '\n' + new_data

# print invalid data in  file "invalid_data.txt"
create_invalid_data_file = open('invalid_data.txt', 'w')
create_invalid_data_file.write(invalid_personal_data)
create_invalid_data_file.close()


                        # print table with new data in file#
###################################################################################

#print(new_data)

openfile.close()

create_new_table_file = open('data_table.txt', 'w')
create_new_table_file.write(str(new_data))
create_new_table_file.close()



