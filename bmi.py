# This program will calculate a persons BMI given height (cm)
# and weight (kg)

#Author: Lonan Keane

#Inputs for weight and height

weight = int(input("enter weight (kg):")) 
height = int(input('enter height (cm):'))

#conversion of cm to meters squared
conversion= (height/100)**2

#BMI calculation
BMI = (weight/conversion)

#show BMI results to user, answer is formatted to 2 decimal places

print("BMI:{:.2f}".format(BMI))