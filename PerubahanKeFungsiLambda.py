import math

a = (lambda x :x**2)(2)
print(a)
b = (lambda x,y : math.sqrt(x**2 + y**2))(2,3)
print(b)
c = (lambda *args : sum(args)/len(args))(2,3)
print(c)
list=["hai","User"]
d = (lambda s : "-".join(set(s)))(list)
print(d)