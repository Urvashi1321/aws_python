import fnmatch
import os

for file in os.scandir("."):
    if fnmatch.fnmatch(file, "*.py"):
        print('Filename : ',file, fnmatch.fnmatch(file, "*.py"))
