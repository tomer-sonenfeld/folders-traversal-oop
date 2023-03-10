import os
from Contents import Directory

#print(os.path.abspath("."))

#x = Directory("x")
#y = Directory("y",x)
#z = Directory("z",y)
#print(x.y.z.printPath())
#print("finish")

#help(os)

#print(os.path.abspath('.'))

x = Directory("x")
y= Directory("y34",x)
z= Directory("z56",y)
print(x.printPath())
print(y.printPath())
print(z.printPath())
print(x.y34.z56.printPath())