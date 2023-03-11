import os
from Directory import Directory
from File import File

def filesThatContains(folder:Directory, word:str):
    files=[]
    for item in folder.getContents():
        if isinstance(item,File):
            if word in item.getContent():
                files.append(item)
        elif isinstance(item,Directory):
            files.extend(filesThatContains(item,word))
    return files

#print(os.path.abspath("."))

#x = Directory("x")
#y = Directory("y",x)
#z = Directory("z",y)
#print(x.y.z.printPath())
#print("finish")

#help(os)

#print(os.path.abspath('.'))

if __name__ == "__main__":
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
    print(filesThatContains(x,"world"))
    print(filesThatContains(x,"abc"))
    print(filesThatContains(x.y,"world"))

