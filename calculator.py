num1 = int(input('enter your first number'))
num2 = int(input('enter your second number:'))

#to repeat action


#define operations
def Addition(num1, num2):
    return num1 + num2
def Subtraction(num1, num2):
    return num1 - num2
def division(num1, num2):
    return num1 % num2
def Multiplication(num1, num2):
    return num1 * num2



operator = input('Enter your operator:')



if operator == '1':
    print(Addition(num1, num2))
    restart = ('y')
    restart = input('Would you like to continue?')
    if restart in('y'):
        num1 = int(input('enter your first number'))
        num2 = int(input('enter your second number:'))
        operator = input('Enter your operator:')
    if restart in('no', 'n'):
       print('Thank you')



elif operator =='2':
    print(Subtraction(num1, num2))
    restart = ('y')
    restart = input('Would you like to continue?')
    if restart in('y'):
        num1 = int(input('enter your first number'))
        num2 = int(input('enter your second number:'))
        operator = input('Enter your operator:')

    if restart in ('no', 'n'):
       print('Thank you')

elif operator =='3':
    print(division(num1, num2))
    restart = ('y')

    restart = input('Would you like to continue?')

if restart in('y'):



  if restart in ('no', 'n'):
    print('Thank you')

elif operator =='4':
    print(Multiplication(num1, num2))
    restart = ('y')
restart = input('Would you like to continue?')
if restart in('y'):


  if restart in ('no', 'n'):
    print('Thank you')

else:
    print('Invalid')







