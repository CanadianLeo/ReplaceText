#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import sys

# Get current directory
directory = os.getcwd()

# If we get less than 3 arguments we print info about using
if (len(sys.argv) == 3):
    findText = sys.argv[1]
    replaceText = sys.argv[2]

    for root, dirs, files in os.walk(directory):
        for filename in files:
            # If current file is executable file we go to the next
            if (filename != os.path.basename(__file__)):

                file = open(root + '/' + filename, 'r')
                fileText = file.read()
                file.close()

                fileText = fileText.replace(findText, replaceText)

                file = open(root + '/' + filename, 'w')
                file.write(fileText)
                file.close()
    
    print('All is done!')
else:
    print('\nError! You need to use:\npython renameText.py old_text new_text\n')
