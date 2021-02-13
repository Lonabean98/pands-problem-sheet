#This program that asks the user to input
# any positive integer and outputs the successive values 
# of the following calculation.
#At each step calculate the next value 
# by taking the current value and, if it is even, divide it by two,
#  but if it is odd, multiply it by three and add one.

#Author:Lonan Keane

#numbers beign calculated will be added into list
numbers= []
#input 
number= int(input("please enter a positive integer: "))

#first number entered is appended into the list
numbers.append(number)
#as long as the number generated is not equal to 1, carry out loop
while number!=1:
   #if number is even,divide by 2 and add to list
   if number%2==0:
      number//=2 
      numbers.append(number)
   #if numebr is odd, multiply by 3 and add 1 and add to list
   else:
      number= int((number*3)+1)
      numbers.append(number)


#print list
print(numbers)
