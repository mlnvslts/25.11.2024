import math

a = float(input("a = "))
b = float(input("b = "))
e = float(input("e = "))
c = float
x = float
result1 = float
result2 = float

while ((b - a) > 2*e):
    c = (a + b)/2
    
    def Fa(a):
        return 2*math.sin(a) - math.atan(a)
    
    result1 = Fa(a)

    def Fc(c):
        return 2*math.sin(c) - math.atan(c)
    
    result2 = Fc(c)
    if result1*result2 < 0:
        b = c
    else:
        a = c

x = (a + b)/2
print(x)