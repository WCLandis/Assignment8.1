import os

directory = input("What directory would you like to save your file into? \n")

if os.path.exists(directory) == True:
	print(f'Working directory {directory} found ')

elif os.path.exists(directory) == False:
	print(f'Directory not found, creating: {directory} directory now.  ')
	os.mkdir(directory)
		
file = input("What is the name of your file? \n")
fullPath = directory+file

name = input('What is your name? \n')
address = input('What is your address? \n')
phone = input('what is your phone number? \n')

with open(fullPath, 'w+') as file_object:
	file_object.write(f"{name}, {address}, {phone}")
	

with open(fullPath, 'r') as file_object:
	userAnswer = file_object.read()
	print(f'You have saved the following information to: {fullPath} \n')
	print(userAnswer)	
