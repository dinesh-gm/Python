# Calculator.py (Version 2)

print("Calculator App - Version 2")

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

print('Choose your action: \n1.Add\n2.Subtract\n3.Multiply\n4.Divide')
calculation = input('Please enter your action: ').lower()


if calculation=='add':
    num3=num1+num2
    print(f'Addition of {num1} and {num2} is {num3}')
elif calculation=='subtract':
    num3=num1-num2
    print(f'Subtraction of {num1} and {num2} is {num3}')
elif calculation=='multiply':
    num3=num1*num2
    print(f'Muliplication of {num1} and {num2} is {num3}')
elif calculation=='divide':
    if num2==0:
        print('Cannot divide by zero')
    else:
        num3=num1//num2
        print(f'Division of {num1} and {num2} is {num3}')
