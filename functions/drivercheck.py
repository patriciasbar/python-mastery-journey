def checkDriverAge(age = 0):
	result = ""
	if int(age) < 18:
		result = f"Sorry, you are too young to drive this car. Powering off"
	elif int(age) > 18:
		result = f"Powering On.Enjoy the ride!"
	elif int(age) == 18:
		result = f"Congratulations on your first year of driving. Enjoy the ride!"
	return result

