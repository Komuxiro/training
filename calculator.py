# simple calculator, count two numbers

a = float(input())
b = float(input())
while True:
    s = input("Enter (+, -, *, /, **): ")
    if s == 0:
        break
    if s in ('+', '-', '*', '/', '**'):
        if s == '+':
            print(a + b)
            break
        if s == '-':
            print(a - b)
            break
        if s == '*':
            print(a * b)
            break
        if s == '**':
            print(a ** b)
            break
        if s == '/':
            if b == 0:
                print('Cannot be divided by zero')
                break
            else:
                print(a / b)
                break
    else:
        print('Invalid operation sign')
