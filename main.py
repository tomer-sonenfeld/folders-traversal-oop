import os
import Directory

if __name__ == '__main__':
    #Probably have to adapt the paths to Linux to make it work there.
    dir1 = Directory.Directory("D:/root_test/")
    print(dir1.lookup_str_in_files("Hello World"))

