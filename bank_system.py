#Bank System
def check_account_number():
	account_number_1 = (input("Enter your account number : "))
	account_number_2 = (input("Re-enter the account number again : "))
	
	if account_number_1 == account_number_2 and len(account_number_1) == len(account_number_2) == 7:
		return True	
	else:
		return False
		

def check_identycard_number():
	identy_card_number = input("Enter the your NIC number : ")
	
	if len(identy_card_number) == 10 or len(identy_card_number) == 15:
		return True
		
	else:
		return False
		

def withdrwal(balance):
	get_money = int(input("How much do u want withdrawal : "))
	
	if (balance - 1000) >= get_money and get_money % 100 ==0 and get_money <= 50000:
		print("Please take your withdrawal")
		now_balance = balance - get_money
		print("Now your account balance is : "+str(now_balance))
	
	elif (balance - 1000) >= get_money and get_money % 100 != 0:
		print("your withdrwal must be 100 multiples ")
	
	elif get_money >= 50000:
		print("You can get less than 50000 per once  ")
		
	else:
		maximum_withdrwal = balance - 1005
		print(" Dear customer, Your acount must be atleast Rs 1000 ")
		print("Your account doesnt has enough money ", " You can withdrwal maximum "+str(maximum_withdrwal), sep = '\n')
		
	print(" ","Thank You !","See you again !", sep = '\n')
	

def deposit(balance):
	print()
	print("Dont put 10, 20, 50 notes into CDMA machine ")
	print()
	
	dep_money = int(input("How much do you would like to deposit : "))
	
	if dep_money % 100 == 0:
		now_balance = balance + dep_money
		print("Your Deposit is success !"," ","Now your account balance : "+str(now_balance), sep = '\n')
		
	else:
		print("please deposit the 100 multiples !")
		
	print(" ","Thank You !","See you again !", sep = '\n')
					
		
def bank_system():
	if check_account_number() == True:
	
		name = input("Enter your name with initials : ")
		
		if check_identycard_number() == True:
			print("Dear customer, Please wait! ")
			print()
			
			last_balance = int(input("Enter the your account balance : "))
			
			print("Dear customer, What do you want ? ")
			print("1 - Deposit", "2 - Withdrwal "," ", sep = '\n')
			
			de_with = int(input("Enter the number what do you want : "))
			
			if de_with == 1:
				deposit(last_balance)
				
			elif de_with == 2:
				withdrwal(last_balance)
				
			else:
				print("Your input is wrong, Try again ")
			
		else:
			print("Dear customer, You entered NIC number is wrong, please enter the details again !") 		
	
	else:
		print("Your account number is wrong, It must be seven digits. Check and Please enter the again")
		
bank_system()
