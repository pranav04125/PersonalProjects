def postfix_calculator(postfix: list):
    stack = []
    
    for i in postfix:
        if i == "+":
            a = stack.pop()
            stack.append(stack.pop() + a)
        elif i == "-":
            a = stack.pop()
            stack.append(stack.pop() - a)
        elif i == "*":
            a = stack.pop()
            stack.append(stack.pop() * a)
        elif i == "/":
            a = stack.pop()
            stack.append(stack.pop() / a)
        elif i == "^":
            a = stack.pop()
            stack.append(stack.pop() ** a)
        elif i.isnumeric():
            stack.append(float(i))
    return stack.pop()