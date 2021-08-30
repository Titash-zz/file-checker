##Class Filechecker whatever

## list {test.py,.gitignore}
## json [{file_name: "test.py", "expected_time": "9 baje"},  {file_name: ".gitignore", "expected_time": "9 baje"}, {file_name: "dddd", "expected_time": "9 baje"}]

## function (path) return list(files,filemetadata)
import sqlite3

from sqlite3 import Error
from app.config.config import get_config
from app.util.file import find_delta
from os import listdir
from os.path import isfile, join
from app.db.db import get_conn

class FileChecker:
    list_of_files = []

    path = "foo"
    config = {}
    def __init__(self,p):
        self.path = p
        self.config = get_config()
        
    
    def process(self) :
        files = listdir(self.path)
        list_from_config = [x["file_name"] for x in self.config]
        missing_files = find_delta(list_from_config, files)
        self.insert()
        if(len(missing_files) > 0 ):

            return {"status": "missing", "missing_file(s)": missing_files}
        else: 
            return {"status": "fileset is complete"}
    
    def insert(self) :
      conn = None
      try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("insert into file_logs values (?, ?, ?)", ("some_name", True, "time"))
        conn.commit()
      except Error as e:
          print(e) 
      finally:
          if conn:
              conn.close()
def main():
    mypath = '/home/titash/file-checker/'
    fc = FileChecker(mypath) 
    print(fc.process())

if __name__ == "__main__":
    main()




