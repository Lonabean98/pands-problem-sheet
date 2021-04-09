#This program will output whether or not today is a weekday.
#Author: Lonan Keane

#This code imports the datetime module
import datetime as dt

#Assigning a variable to the current date
today = dt.datetime.now()

#Strftime() formats the date object as a readable string
#%A formats the date as a full Weekday
#If the result is Saturday or Sunday, it will say it is the weekend
weekend= ["Saturday", "Sunday"]
if (today.strftime("%A")) in weekend:
    print("It is the weekend, yay!")
#if the result is not Saturday or Sunday, it will say it is not 
# the weekend
else:
    print("Yes, unfortunately today is a weekday")