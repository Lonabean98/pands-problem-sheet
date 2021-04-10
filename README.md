# pands-problem-sheet
## Introduction
This readme file explains the code in each of the weekly tasks for the Programming and Scripting module for Data Analytics 2021

## TASK 2:
Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

### Code: 
![image](https://user-images.githubusercontent.com/77697552/114286405-4a56ce80-9a56-11eb-9898-dc9df59ce3b7.png)


### Explanation:
User is prompted to enter the weight and height. Both of these inputs are converted to integers. The variable "conversion" divides the height by 100 and multiplies this answer by 2. The BMI is calculated by dividing the weight by the conversion variable. The BMI value is then printed to 2 decimal places. 

## TASK 3:
Write a program that asks a user to input a string and outputs every second letter in reverse order.

### Code:
![image](https://user-images.githubusercontent.com/77697552/114286426-868a2f00-9a56-11eb-9ca3-6290207a568d.png)


### Explanation:
The user is asked to enter a string, which is stored in the "firstSentence" variable. The reverse slice function is then used to take out every second letter. 

## TASK 4:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

### Code: 
![image](https://user-images.githubusercontent.com/77697552/114286443-ad486580-9a56-11eb-97ef-8febcfc4f71d.png)

### Explanation:
1. Numbers is an empty list.
2. User is asked to input a positive integer. This input is then appended to the numbers list.
3. For any input other than 1, if the remainder of the input divided by 2 is 0, it is divided by two and appended to the list. If the remainder divided by 2 is not 0, the number is multiplied by 3 and 1 is added. This is also appended to the list.
4. The "numbers" list is printed.

## TASK 5:
Write a program that outputs whether or not today is a weekday.

### Code: 
![image](https://user-images.githubusercontent.com/77697552/114286451-c8b37080-9a56-11eb-9814-0382cf90f276.png)

### Explanation:
1. datetime module is imported as "dt".
2. datetime.now() retrieves the current date and time and is given the variable "today". 
3. strftime() formats the date object as a readable string. If the current date is in the "weekend" list, it will print "It is the weekend, yay!".
4. If not, it will print "Yes, unfortunately today is a weekday" (Joiner, 2011) 

## TASK 6:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

### Code:
![image](https://user-images.githubusercontent.com/77697552/114286462-dd900400-9a56-11eb-92e1-17d9a3d607eb.png)


### Explanation:
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


## TASK 7:
Write a program that reads in a text file and outputs the number of e's it contains.

### Code:
![image](https://user-images.githubusercontent.com/77697552/114286476-ef71a700-9a56-11eb-9d93-0f97289c77e8.png)


### Explanation:
1. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. (sys — System-specific parameters and functions, n.d.) 
2. sys.argv returns a list of command line arguments passed to a Python script.
3. opening the argument as f.
4. The text in the file is read into a string.
5. The starting point of "e_count" is 0.
6. Looping through each character in the text. If the letter is "e", 1 will be added to the e_count variable. 
7. Final e_count is printed.

## TASK 8:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

### Code: 
![image](https://user-images.githubusercontent.com/77697552/114286489-0d3f0c00-9a57-11eb-956f-c22e457940f7.png)


### Explanation:
1. numpy and matplotlib.pyplot are imported.
2. linspace returns evenly spaced numbers over a specified interval, in this case 0 to 4. (numpy.linspace, 2021)
3. naming the label for each function.
4. added second line. 2 is superscripted to create 2 squared. (Superscript in Python plots, 2014) 
5. Added third line. 3 is superscripted. 
6. Placed a legend in the upper left hand corner of the plot. (Adding a legend to PyPlot in Matplotlib in the simplest manner possible, 2020) 
7. Added title to plot. 
8. Added grid. 
9. Show or save figure. 

## References:

Adding a legend to PyPlot in Matplotlib in the simplest manner possible. (2020, February 4). Retrieved from stackoverflow.com: https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible

Hatterer, R. (2020, July 29). datasets.load_iris() in Python. Retrieved from Stackoverflow: https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python

Joiner, M. (2011, December 5). How to get day name from datetime. Retrieved from Stackoverflow: https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime

numpy.linspace. (2021, January 31). Retrieved from numpy.org: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

Superscript in Python plots. (2014, January 20). Retrieved from stackoverflow.com: https://stackoverflow.com/questions/21226868/superscript-in-python-plots

sys — System-specific parameters and functions. (n.d.). Retrieved from docs.python.org: https://docs.python.org/3/library/sys.html



