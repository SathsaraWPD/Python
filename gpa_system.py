#Calculate the GPA System

def subject_select ():
	
	print(" ", "Enter the your subjects credits :- ", sep = '\n')
	
	course_credit_array = []
	course_credit_array = list(map(int,input().split()))
	length_subject = len(course_credit_array)
	
	sum1 = 0
	for i in range(length_subject):
		sum1 = sum1 + course_credit_array[i]
		
	
	print("Enter the grade number for as you did subject respectively :")
	course_grade_array = []
	course_grade_array = list(map(float, input().split()))
	length_grade = len(course_grade_array)
	print()
	
	sum2 = 0
	if length_subject == length_grade :
	
		for x , y in zip(course_credit_array, course_grade_array):
			sum2 = sum2 + (x*y)	
		print("You got total of credits : "+str(sum2))
		
			
		print(" ", "Your Semester GPA : ", sep = '\n' )
		gpa = sum2 / sum1
		print(gpa," "," ", sep = '\n')	
		
		print("Your Status :-")
		
		if gpa >= 3.7:
			print("First Class ")
		elif gpa >= 3.3:
			print("Second Upper")
		elif gpa >= 3.0:
			print("Second Lower")
		else:
			print("General")
			
		print(" "," ","Congratulation......!"," ","Wish you all the best.....! ", sep = '\n')
		
	else:
		print("Your input is incorrect... Please check again ! ")





def combined_program():

	examination_number = input("Enter the Index number : ")
	name = input("Enter Your Name with initial : ")
	
	print(" ","You can select number as you got result :- "," ",sep = '\n')
	
	print ("A+ :- 4.0", "A :- 4.0", "A- :- 3.7", "B+ :- 3.3", "B :- 3.0", "B- :- 2.7", "C+ :- 2.3", "C :- 2.0", "C- :- 1.7", "D+ :- 1.3","D :- 1.0", "E :- 0.0", sep = '\n')
	
	subject_select()

combined_program()


