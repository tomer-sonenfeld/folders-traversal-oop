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
    # files_scanner = Search()
    # result = files_scanner.search_by_content('/path/to/root/dir', 'the-word-to-look-for')

    # result should include list of all paths that has the searched word..



