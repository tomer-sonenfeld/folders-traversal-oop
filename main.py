import os
from Contents import Directory
from Contents import File
from Contents import filesThatContains

#print(os.path.abspath("."))

#x = Directory("x")
#y = Directory("y",x)
#z = Directory("z",y)
#print(x.y.z.printPath())
#print("finish")

#help(os)

#print(os.path.abspath('.'))

x = Directory("x")
x.addSubfolder(Directory("y",x))
x.y.addSubfolder(Directory("z",x.y))
x.y.z.addFile(File("someFile","hello world",x.y.z))
x.y.addFile(File("someFile2","hello",x.y))
#y= Directory("y34",x)
#z= Directory("z56",y)
#print(x.printPath())
#print(y.printPath())
#print(z.printPath())
#print(x.y34.z56.printPath())
print(x.y.z.printPath())
print(x.y.z.someFile.printPath())
x.y.z.someFile.printContent()

print(filesThatContains(x,"hello"))

