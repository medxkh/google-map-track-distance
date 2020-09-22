import requests
import smtplib


api_file = open("api_key","r")

api_key = api_file.read()
api_file.close()


home = input("Enter your Home adrss")
work = input("Enter your work adrss")

base url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"


r = requests.get(url+"origins"+home+"&destinations="+work+"&key"+api_key)