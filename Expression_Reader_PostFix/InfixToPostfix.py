from cmath import inf
from turtle import position


def postfix(infix: str, index_return: bool = False):
    stack = []
    postfix_expression = []
    operator_order = {"^" : 1,
                      "/" : 2,
                      "*" : 2,
                      "-" : 3,
                      "+" : 3}
    current_number = ""
    
    i = 0
    while i < len(infix):
        if infix[i] in operator_order.keys():
            postfix_expression.append(current_number)
            current_number = ""
            if stack:
                if operator_order.get(stack[-1], 0) <= operator_order[infix[i]]:
                    postfix_expression.append(stack.pop())
                    continue
            stack.append(infix[i])
        elif infix[i] == '(':
            post, index = postfix(infix[i + 1 : ], True)
            postfix_expression.extend(post)
            i += index + 1

        elif infix[i] == ')':
            break
        elif infix[i].isspace():
            pass
        else:
            current_number += infix[i]
        
        i += 1

    postfix_expression.append(current_number)

    while stack:
        postfix_expression.append(stack.pop())

    if index_return:
        return postfix_expression, i
    return postfix_expression