import os
from Directory import Directory

#print(os.path.abspath("."))

x = Directory("x")
y = Directory("y",x)
z = Directory("z",y)
print(x.y.z.printPath())
print("finish")