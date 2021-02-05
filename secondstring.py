#This program asks a user to input a string 
# and outputs every second letter in reverse order.

#Author: Lonan Keane

# User input formatted as string
firstSentence = str(input("please enter a sentence:")) 

#here, the input is
#being reduced to every second character using the reverse slice function
output = (firstSentence[::-2]) 

#print output to user
print(output)   