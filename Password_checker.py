passwd = input("Enter password: ")
symbol = "!@#$%^&*()-+"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digits = '1234567890'
all = (symbol + upper + lower + digits)

for i in range(len(passwd)):
    if passwd[i] not in all:
        err = 1
        break
    else:
        err = 0

if len(passwd) < 12:
    x = 12 - len(passwd)
    l = 0
else:
    l = 1

for i in range(len(upper)):
    if upper[i] in passwd:
        a = 1
        break
    else:
        a = 0

for i in range(len(lower)):
    if lower[i] in passwd:
        b = 1
        break
    else:
        b = 0

for i in range(len(digits)):
    if digits[i] in passwd:
        c = 1
        break
    else:
        c = 0

for i in range(len(symbol)):
    if symbol[i] in passwd:
        d = 1
        break
    else:
        d = 0
if err == 1:
    print("Error. Restricted symbol.")
elif a + b + c + d + l == 5:
    print("Strong password.")
elif a + b + c + d + l != 5:
    print("Weak password. Recomended: ", end='')
    if l == 0:
        print(f"add {x} symbols", end=', ')
    if a == 0:
        print(f"add 1 upper letter", end=', ')
    if b == 0:
        print(f"add 1 lower letter",end=', ')
    if c == 0:
        print(f"add 1 digit", end=', ')
    if d == 0:
        print(f"add 1 special symbol", end='')