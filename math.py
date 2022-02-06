# Add Implementation
def Add(x,y):
    return x+y

# Subtract Implementation
def Subtract(x,y):
    return x-y      #on Master branch

# Multiply Implementation
def Multiply(x,y):
    return x*y    #on Bug456 branch

# Divide Implementation    
def Divide(x,y):
    if y==0:            #on Master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
# Square implementation  
def square(x):
    return x*x