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
while True : 
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
	ch = int(input("Enter the choice"))
	if ch is None:
		print("Enter valid choice ")
	elif ch == 1:
		emp_id  = int(input("Enter id"))
		if emp_id not in employee.keys():
			emp_name  = input("Enter name")
			emp_age = int(input("Enter age"))
			emp_gender = input("Gender")
			emp_place = input("Enter place")
			emp_sal = input ("Enter salary")
			emp_prevcomp = input("Enter previous company")
			emp_joindate = input("Enter joined date")
			temp = {
			"emp_name" : emp_name,
			"emp_age" : emp_age,
			"emp_gender" : emp_gender,
			"emp_sal" : emp_sal,
			"emp_place" : emp_place,
			"emp_joindate" : emp_joindate,
			"emp_prevcomp" : emp_prevcomp
			}
			employee[emp_id] = temp
	   		
	elif ch == 2:
		emp_id = int(input("Enter employee ID"))
		if emp_id not in employee:
			print("Enter valid Emp_ID")
		else:
			del employee[emp_id]
	elif ch == 3:
		name = input("Enter the name to be search")
		flag = False
		for ename in employee.values():
			if ename["emp_name"] == name :
				flag = True
		if flag == True:
			print(f"{name} is found")
		else:
			print(f"{name} is not found")	
		
	elif ch == 4:
		emp_id = int(input("Enter employee id"))
		print("Change employee data")
		print("\ta. Change Name")
		print("\tb. Change age")
		print("\tc. Change gender")
		print("\td. Change salary")
		choice = input("\tEnter the choice")
		if emp_id in employee.keys():
			if choice == "a":
				name = input("Enter new name")
				employee[emp_id]["emp_name"] = name
			elif choice == "b":
				age = input("Enter new age")
				employee[emp_id]["emp_age"] = age
			elif choice == "c":
				gender = input("Enter new gender")
				employee[emp_id]["emp_gender"] = gender
			elif choice == "d":
				sal = input("Enter new salary")
				employee[emp_id]["emp_sal"] = sal
			else:
				print("Wrong choice")
	elif ch == 5:
		print(employee)
		for emp_id,emp_det in employee.items():
			print(f"{emp_id} | {emp_det['emp_name']} | {emp_det['emp_age']} | {emp_det['emp_gender']} | {emp_det['emp_sal']}")
	elif ch == 6:
		break
	else:
		print("Invalid choice")
	
	
	
