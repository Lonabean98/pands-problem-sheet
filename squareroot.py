#This program takes an input and outputs an approximation of its square root
#Author: Lonan Keane

#x is the input, converted to a float
x = float(input("Please enter a positive number: "))  

#defining sqrt function
def sqrt(x):
   #The tolerance is the limit of the difference between the input and 
   #squared Newton approximation
   tolerance = 0.000001
   #The estimation is formatted as half of the input value
   guess = x/2
   #This statement will loop indefinitely until 
   # the return condition is met
   while True:
        #This changes the value of guess to the result of the Newton
        #equation
        guess = (guess + x / guess) / 2
        #variable to describe the absolute
        #difference between the input and the Newton Approximation
        difference = abs(x - guess ** 2)
        #if the tolerance is greater than the difference between 
        # Newton approximation and input, it will stop the loop
        if difference <= tolerance:
            break
   #Returns the final Newton approximation
   return guess
#Runs the sqrt function using input x 
sqrt(x)
#print results of sqrt function rounded to 1 decimal place
print("The square root of {} is approx" .format(x), round(sqrt(x), 1))