from Search import Search

if __name__ == "__main__":

    files_scanner = Search()
    result= files_scanner.search_by_content(r"C:\Users\tomer\PycharmProjects\Training\testFolder","hello")
    print(result)






