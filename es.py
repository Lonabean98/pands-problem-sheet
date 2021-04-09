#This program reads in a text 
#file and outputs the number of e's it contains.
#It can also take the filename from an argument on the command line.
#Author: Lonan Keane

#The sys module provides functions and variables used to 
# manipulate different parts of the Python runtime environment.
import sys
# sys.argv returns a list of command line arguments 
# passed to a Python script.
filename= sys.argv[1]
#opening the argument as f
with open(filename) as f:
    #reads all the text from a file into a string. 
    x=f.read()
    #This is the start of the e count
    e_count= 0
    #looping through every character in the file
    for letter in x:
       if letter =='e' or letter== 'E':
        # if the letter is e or E, add one to the e count
        e_count += 1
    #print the final e count
    print(e_count)