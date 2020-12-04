def Lam(variable, application):
    if isinstance(variable, tuple):
        if len(variable) > 1:
            curried = ('_Lam', variable[0], Lam(variable[1:], application))
            return curried
        else:
            currying = ('_Lam', variable[0], application)
            return currying
    else:
        no_need_currying = ('_Lam', variable, application)
        return no_need_currying

def App(E1, E2):
    t1 = ('_App', E1, E2)
    return t1

def IsFreeVariable(variable, expression):
    if isinstance(expression, str):
        if variable == expression:
            return True
        else:
            return False   

    if IsFreeVariable(variable, expression[1]):
        return True
    if IsFreeVariable(variable, expression[2]):
        return True

    return False

def BracketAbstraction(lambda_expression):
    if isinstance(lambda_expression, str): # 1
        return lambda_expression
    elif lambda_expression[0] == '_App': # 2
        return App(BracketAbstraction(lambda_expression[1]), BracketAbstraction(lambda_expression[2]))
    elif lambda_expression[0] == '_Lam' and not IsFreeVariable(lambda_expression[1], lambda_expression[2]): # 3
        return App('K', BracketAbstraction(lambda_expression[2]))
    elif lambda_expression[0] == '_Lam' and lambda_expression[1] == lambda_expression[2]: # 4
        return 'I'
    elif lambda_expression[0] == '_Lam' and lambda_expression[2][0] == '_Lam' and IsFreeVariable(lambda_expression[1], lambda_expression[2][2]): # 5
        return BracketAbstraction(Lam(lambda_expression[1], BracketAbstraction(lambda_expression[2])))
    elif lambda_expression[0] == '_Lam' and lambda_expression[2][0] == '_App':
        if IsFreeVariable(lambda_expression[1],lambda_expression[2][1]) or IsFreeVariable(lambda_expression[1],lambda_expression[2][2]): # 6
            return App(App('S', BracketAbstraction(Lam(lambda_expression[1], lambda_expression[2][1]))), BracketAbstraction(Lam(lambda_expression[1], lambda_expression[2][2])))

def ppExp(expression):
    if isinstance(expression, tuple):
        if expression[0] == '_App':
            return '(' + ppExp(expression[1]) + ppExp(expression[2]) + ')'
        else:
            return '\\' + ppExp(expression[1]) + '.' + ppExp(expression[2])
    else:
        return expression


# for test

example = Lam(("x", "y"), App("y", "x"))
add = Lam(("m", "n", "f", "x"), App(App("m", "f"), App(App("n", "f"), "x")))
succ = Lam(("n", "f", "x"), App("f", App(App("n", "f"), "x")))
zero = Lam(("f", "x"), "x")
one = Lam(("f", "x"), App("f", "x"))

print('\n\n내부 구조 출력\n\n')

print(example)
print(add)
print(succ)
print(zero)
print(one)

print('\n\nppExp 내부 구조 출력\n\n')

print(ppExp(example))
print(ppExp(add))
print(ppExp(succ))
print(ppExp(zero))
print(ppExp(one))

print('\n\nBracketAbstraction 출력\n\n')

print(BracketAbstraction(example))
print(BracketAbstraction(add))
print(BracketAbstraction(succ))
print(BracketAbstraction(zero))
print(BracketAbstraction(one))

print('\n\nppExp BracketAbstraction 출력\n\n')

print(ppExp(BracketAbstraction(example)))
print(ppExp(BracketAbstraction(add)))
print(ppExp(BracketAbstraction(succ)))
print(ppExp(BracketAbstraction(zero)))
print(ppExp(BracketAbstraction(one)))

print("\n\nAdd 1 1 출력\n\n")
print(ppExp(BracketAbstraction(add)) + ppExp(BracketAbstraction(one)) + ppExp(BracketAbstraction(one)))