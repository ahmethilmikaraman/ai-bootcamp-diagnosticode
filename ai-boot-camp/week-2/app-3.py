
var = 10 

def increase():
    global var
    var +=1

def decrease():
    global var
    var -=1

increase() # var = 11
increase() # var = 12
increase() # var = 13
increase() # var = 14
decrease() # var = 13

print(var)