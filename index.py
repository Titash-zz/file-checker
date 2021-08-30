from app.file_checker import  FileChecker 
from app.db.db import init_queries
def main():
    init_queries()
    mypath = '/home/titash/file-checker/'
    fc = FileChecker(mypath) 
    print(fc.process())

if __name__ == "__main__":
    main()