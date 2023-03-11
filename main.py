from Directory import Directory
from File import File

def filesThatContains(folder:'Directory', word:str):
    files=[]
    for item in folder.contents:
        if isinstance(item,File):
            if word in item.content:
                files.append(item)
        elif isinstance(item,Directory):
            files.extend(filesThatContains(item,word))
    return files


if __name__ == "__main__":
    x = Directory("x")
    x.add_subfolder(Directory("y", x))
    x.y.add_subfolder(Directory("z", x.y))
    x.y.z.add_file(File("someFile", "hello world", x.y.z))
    x.y.add_file(File("someFile2", "hello", x.y))
    #y= Directory("y34",x)
    #z= Directory("z56",y)
    #print(x.printPath())
    #print(y.printPath())
    #print(z.printPath())
    #print(x.y34.z56.printPath())
    print(x.y.z.print_path())
    print(x.y.z.someFile.print_path())
    x.y.z.someFile.print_content()

    print(filesThatContains(x,"hello"))
    print(filesThatContains(x,"world"))
    print(filesThatContains(x,"abc"))
    print(filesThatContains(x.y,"world"))
    #x.y.z.someFile.addFile(x.y.someFile2)

