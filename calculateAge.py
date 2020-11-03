print("The date is as follows ")
import datetime
now=datetime.datetime.now()
print(now.year, now.month, now.day)
name=input("Hi. Please enter your name ")
print("Hello",name)
age=int(input("Please enter your age and also enter in which year you will be so old "))
print("You are going to be 100 on the year",(now.year-age+100))
input()