# pands-problem-sheet
Introduction
This readme file explains the code in each of the weekly tasks for the Programming and Scripting module for Data Analytics 2021


##TASK 2:
bmi.py:
This takes an input of height in cm and weight in kg and calculates the BMI

###Code: 
weight = int(input("enter weight (kg):")) 
height = int(input('enter height (cm):'))
conversion= (height/100)**2
BMI = (weight/conversion)
print("BMI is :{:.2f}".format(BMI))

###Explanation:
User is prompted to enter the weight and height. Both of these inputs are converted to integers. The variable "conversion" divides the height by 100 and multiplies this answer by 2. The BMI is calculated by dividing the weight by the conversion variable. The BMI value is then printed to 2 decimal places. 

##TASK 3:
Write a program that asks a user to input a string and outputs every second letter in reverse order.

###Code:
firstSentence = str(input("please enter a sentence:")) 
output = (firstSentence[::-2]) 
print(output)   

###Explanation:
The user is asked to enter a string, which is stored in the "firstSentence" variable. The reverse slice function is then used to take out every second letter. 

##TASK 4:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

###Code: 
numbers= []
number= int(input("please enter a positive integer: "))
numbers.append(number)
while number!=1:
   if number%2==0:
      number//=2 
      numbers.append(number)
   else:
      number= int((number*3)+1)
      numbers.append(number)
print(numbers)


###Explanation:
1. Numbers is an empty list
2. User is asked to input a positive integer. This input is then appended to the numbers lsit.
3. For any input other than 1, if the remainder of the input divided by 2 is 0, it is divided by two and appended to the list. If the remainder divided by 2 is not 0, the number is multiplied by 3 and 1 is added. This is also appended to the list.
4. The "numbers" list is printed.


##TASK 5:
Write a program that outputs whether or not today is a weekday.

###Code: 
import datetime as dt
today = dt.datetime.now()
weekend= ["Saturday", "Sunday"]
if (today.strftime("%A")) in weekend:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")


###Explanation:
1.datetime module is imported as "dt".
2.datetime.now() retrieves the current date and time and is given the variable "today". 
3.strftime() formats the date object as a readable string. If the current date is in the "weekend" list, it will print "It is the weekend, yay!".
4. If not, it will print "Yes, unfortunately today is a weekday" Reference: https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime


##TASK 6:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

###Code:
x = float(input("Please enter a positive number: "))  
def sqrt(x):
   tolerance = 0.000001
   guess = x/2
   while True:
        guess = (guess + x / guess) / 2
        difference = abs(x - guess ** 2)
        if difference <= tolerance:
            break
   return guess
sqrt(x)
print("The square root of {} is approx" .format(x), round(sqrt(x), 1))

###Explanation:
1. Asks the user to input a positive integer.
2. Defining the function sqrt(x)
3. The tolerance is the limit of the difference between the input and squared Newton approximation
4. The "guess" variable is the input divided by 2. 
5. "while True" will make the following statment loop indefinitely. 
6. "Guess" is  changed  to the result of the Newton equation
7. "Difference" is a variable to describe the absolute difference between the input and the Newton Approximation
8. If the tolerance is greater than the difference between the Newton approximation and input, it will stop the loop
9. Returns the final Newton approximation
10. sqrt() function is run using x as the argument. 
11. Results of sqrt function is printed rounded to 1 decimal place.



##TASK 7:
Write a program that reads in a text file and outputs the number of e's it contains.

###Code:
import sys
filename= sys.argv[1]
with open(filename) as f:
    x=f.read()
    e_count= 0
    for letter in x:
       if letter =='e' or letter== 'E':
        e_count += 1
    print(e_count)

###Explanation:
1. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Reference: https://docs.python.org/3/library/sys.html
2. sys.argv returns a list of command line arguments passed to a Python script. https://www.tutorialsteacher.com/python/sys-module.
3. opening the argument as f.
4. The text in the file is read into a string.
5. The starting point of "e_count" is 0.
6. Looping through each character in the text. If the letter is "e", 1 will be added to the e_count variable. 
7. Final e_count is printed.


##TASK 8:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

###Code: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4)
y=  x
plt.plot(x,y, label= "f(x)= x")

x2= np.linspace(0,4)
y2= x2**2
plt.plot(x2,y2, label= "g(x)= $x^2$")

x3= np.linspace(0,4)
y3= x3 **3
plt.plot(x3, y3, label= "h(x)= $x^3$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.title("plottask.py")
plt.grid()
plt.show()


###Explanation:
1. numpy and matplotlib.pyplot are imported.
2. linspace returns evenly spaced numbers over a specified interval, in this case 0 to 4. Reference: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
3. naming the label for each function.
4. added second line. 2 is superscripted to create 2 squared. Reference: https://stackoverflow.com/questions/21226868/superscript-in-python-plots
5. Added third line. 3 is superscripted. 
6. Placed a legend in the upper left hand corner of the plot. Reference: https://stackoverflow.com/questions/19125722/adding-a-
legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible

7. Added title to plot. 
8. Added grid. 
9. Show or save figure. 

I got the code for the day of the week from https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime

References:

squareroot.py:
This program takes an input and outputs the square root using Newtons approximation method.
I referenced the code from https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots in this program

es.py:
I found out the method to take an argument from a filename from https://www.tutorialsteacher.com/python/sys-module. I tested that this worked by downloading a different txt file from the internet and inputting their names as an argument, which worked.

plottask.py:
This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. I got the code to place a legend from: https://stackoverflow.com/questions/19125722/adding-a-
legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible

I got to code to superscript number from: https://stackoverflow.com/questions/21226868/superscript-in-python-plots