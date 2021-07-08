#ADD
def add(x,y):
    return x+y

#SUBTRACT
def subtract(x,y):
    return x-y          #on master branch

#MULTIPLY
def multiply(x,y):
    return x*y          #on Bug456 branch

#DIVIDE
def divide(x,y):        #on Bug789 branch
    if y==0:
        return DIVIDE_BY_0_ERROR
    else:
        return x/y