from InfixToPostfix import postfix
from PostfixCalculator import postfix_calculator

while True:
    exp = input("> ")
    
    if exp == 'q':
        break
    print(postfix_calculator(postfix(exp)))