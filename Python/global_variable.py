
a = 14

def something():
    global a
    a = 29
    print("Local variable",a)

something()

print("globle variable",a)