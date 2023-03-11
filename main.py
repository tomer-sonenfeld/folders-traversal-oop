from Directory import Directory
from File import File

def files_that_contains(folder: 'Directory', word:str):
    files=[]
    for item in folder.contents:
        if isinstance(item,File):
            if word in item.content:
                files.append(item)
        elif isinstance(item,Directory):
            files.extend(files_that_contains(item, word))
    return files


if __name__ == "__main__":
    x = Directory("x")
    x.add_subfolder(Directory("y", x))
    x.y.add_subfolder(Directory("z", x.y))
    x.y.z.add_file(File("someFile", "hello world", x.y.z))
    x.y.add_file(File("someFile2", "hello", x.y))
    print(x.y.z.print_path())
    print(x.y.z.someFile.print_path())
    x.y.z.someFile.print_content()

    print(files_that_contains(x, "hello"))
    print(files_that_contains(x, "world"))
    print(files_that_contains(x, "abc"))
    print(files_that_contains(x.y, "world"))

