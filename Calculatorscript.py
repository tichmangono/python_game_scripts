#Returns the sum of num1 and num2
def add(num1,num2):
	return num1 + num2
#Returns the difference of num1 and num2
def sub(num1,num2):
	return num1 - num2
#Returns the multiple of num1 and num2
def mult(num1,num2):
	return num1 * num2
#Returns the divisor of num1 and num2
def div(num1,num2):
	return num1 / num2	
	
	
def main():
	operation=input("What do you want to do?(+,-,*,/): ")
	if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		# invalid operation
		print ("You must enter a valid operation")
	else:
		var1 = int(input("Enter var1: "))
		var2 = int(input("Enter var2: "))
		if (operation== '+'):
			print(add(var1,var2))
		elif (operation =='-'):
			print(sub(var1,var2))
		elif (operation =='*'):
			print(mult(var1,var2))
		else:
			print(div(var1,var2))			
main()