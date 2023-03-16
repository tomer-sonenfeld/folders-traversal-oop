import os

from search import Search

if __name__ == "__main__":
    files_scanner = Search()
    result= files_scanner.search_by_content(os.getcwd(),"hello")
    print(result)






