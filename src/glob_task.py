import glob
import os
#Directory where files are to be searched
directory = 'C:/Users/7000033086/Documents/aws_python/src'

#File patterns that are to be searched
file_patterns = ['*.py', '*.txt']

#Iterate through the file patterns and search for files
for pattern in file_patterns:
    #glob.glob function to find files that match the pattern
    files = glob.glob(f"{directory}/{pattern}")

    #Print the list of files found for the current pattern
    print(f"Files matching pattern '{pattern}':")
    for file in files:
        print(file)
