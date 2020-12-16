#the syntax is 
#if condition == True:
	#do this
#there's 3 types of if statement, which is IF,ELIF,ELSE
#if you use "elif" Statement, python will read continuosly from top to bottom until the condidions is True

print('Put your Weight here:')
Weight=input()
if int(Weight) <=37:
	print("wow you're thin, so you can't enter")
elif int(Weight) ==100:
	print("wow you're Ideal")
elif int(Weight) >=60:
	print("wow you're fat, so you can't enter")
else:
	print("You can Enter here, Congratulations")