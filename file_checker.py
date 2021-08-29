##Class Filechecker whatever

## list {test.py,.gitignore}
## json [{file_name: "test.py", "expected_time": "9 baje"},  {file_name: ".gitignore", "expected_time": "9 baje"}, {file_name: "dddd", "expected_time": "9 baje"}]

## function (path) return list(files,filemetadata)

from config.config import get_congif
from util.file_util import find_delta
from os import listdir
from os.path import isfile, join


class FileChecker:
    list_of_files = []

    path = "foo"
    config = {}
    def __init__(self,p):
        self.path = p
        self.config = get_congif()
        
    
    def process(self) :
        files = listdir(self.path)
        list_from_config = [x["file_name"] for x in self.config]
        missing_files = find_delta(list_from_config, files)
        if(len(missing_files) > 0 ):
            return {"status": "missing", "missing_file(s)": missing_files}
        else: 
            return {"status": "fileset is complete"}
    

def main():
    mypath = '/home/titash/file-checker/'
    fc = FileChecker(mypath) 
    print(fc.process())

if __name__ == "__main__":
    main()




