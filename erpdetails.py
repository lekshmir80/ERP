#Console ERP project
#Implement using dictionary:
#	-Add Employee
#	-Delete Employee
#	-Search Employee by name
#	-Change Employee Data
#		=>Change name
#		=>change age
#		=>Change gender
#		=>change salary
#	-Display 

#Properties:Empid, Name,age,gender,place,salary,previous_company,joining_date
#Date format "21/04/2021" dd/mm/yyyy



employee = {}

def menu():
	print("1. Add Employee")
	print("2. Delete Employee")
	print("3. Search Employee")
	print("4. Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
	print("5. Display")
	print("6. Exit")


def add_employee():
	print("Add Employee")
	emp_id  = int(input("Enter id"))
	if emp_id not in employee.keys():
		employee[emp_id]  = {
			"emp_name" : input("Enter name"),
			"emp_age" : int(input("Enter age")),
			"emp_gender" : input("Gender"),
			"emp_sal" : input ("Enter salary"),
			"emp_place" : input("Enter place"),
			"emp_joindate" : input("Enter joined date"),
			"emp_prevcomp" : input("Enter previous company")
		}
	else:
		print("employee ID already taken")

def delete_employee():
	print("Delete Employee")
	emp_id = int(input("Enter employee ID"))
	if emp_id not in employee:
		print("Enter valid Emp_ID")
	else:
		del employee[emp_id]
		
def search_employee():
	print("Search employee by name")
	name = input("Enter the name to be search")
	flag = False
	for ename in employee.values():
		if ename["emp_name"] == name :
			flag = True
	if flag == True:
		print(f"{name} is found")
	else:
		print(f"{name} is not found")	
		
def update_menu():
	print("Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
	
def update_empoyee():
	emp_id = int(input("Enter employee id"))
	update_menu()
	choice = input("\tEnter the choice")
	if emp_id in employee.keys():
		if choice == "a":
			name = input("\tEnter new name")
			employee[emp_id]["emp_name"] = name
		elif choice == "b":
			age = input("\tEnter new age")
			employee[emp_id]["emp_age"] = age
		elif choice == "c":
			gender = input("\tEnter new gender")
			employee[emp_id]["emp_gender"] = gender
		elif choice == "d":
			sal = input("\tEnter new salary")
			employee[emp_id]["emp_sal"] = sal
		else:
			print("Wrong choice")
def display_employee():
	for emp_id,emp_det in employee.items():
		print(f"{emp_id} | {emp_det['emp_name']} | {emp_det['emp_age']} | {emp_det['emp_gender']} | {emp_det['emp_sal']}")
while True : 
	menu()
	ch = int(input("Enter the choice"))
	if ch is None:
		print("Enter valid choice ")
	elif ch == 1:
		add_employee()	
	elif ch == 2:
		delete_employee()
	elif ch == 3:
		search_employee()	
	elif ch == 4:
		update_empoyee()
	elif ch == 5:
		display_employee()		
	elif ch == 6:
		break
	else:
		print("Invalid choice")
	
	
	
