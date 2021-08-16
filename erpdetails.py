#Console ERP project August 12
#Implement using dictionary => then functions:
#	-Add Employee
#	-Delete Employee
#	-Search Employee(updated)
#		-search by name(new)- August 16
#		-search by age(new)August 16
#		-search by salary(new)August 16
#		-search by gender(new)August 16
#	-Change Employee Data
#		=>Change name
#		=>change age
#		=>Change gender
#		=>change salary
#	-Display 
#Properties:Empid, Name,age,gender,place,salary,previous_company,joining_date
#Date format "21/04/2021" dd/mm/yyyy

'''August 13 added manage group functionality
-(New)Manage Teams
	--Edit organization(New)
		-Create new Team
		-Display team
		-Manage Team(Particular Team)
			-Rename Team(optional)
			-Display Members
			-Add Members
			-Delete Members
		-Delete Team
'''
employee = {}
organisation = {}
teams = {}
def menu():
	print("1. Add organization Details")
	print("2. Edit Organization Details")
	print("3.View organisation Details")
	print("4. Add Employee")
	print("5. Delete Employee")
	print("6. Search Employee")
	print("7. Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
	print("8. Manage Team")
	print("9. Display")
	print("10. Exit")


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
def search_employee_options():
	search_menu()
	ch = input("Enter the choice")
	if ch == "a":
		name = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_name"] == name,employee.values())))
	elif ch == "b":
		age = int(input("Enter the name to be search"))
		print(list(filter(lambda a: a["emp_age"] == age,employee.values())))
	elif ch == "c":
		gender = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_gender"] == gender,employee.values())))
	elif ch == "d":
		salary = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_sal"] == salary,employee.values())))
	else:	
		print("Invalid choice")
def search_employee():# Currently not using
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
def search_menu():
	print("Change employee data")
	print("\ta. search by Name")
	print("\tb. search by age")
	print("\tc. search by gender")
	print("\td. search by salary")
	print("\te. Exit")		
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

def manage_gpmenu():
	print("\ta.Create Team")
	print("\tb.Display Teams")
	print("\tc.Manage Team(Particular)")
	manage_member_menu()
	print("\td.Delete Team")
	print("\te.Exit")

def create_team():
	team_name = input("Enter the team name")
	teams[team_name] = []

def display_teams():
	for key,teamlist in teams.items():
		name_string = ""
		for i in teamlist:
			name_string = name_string + "|" +employee[i]["emp_name"]
		print(f"{key} => {name_string}")
def delete_team():
	team_name = input("Enter the team name")
	if team_name in teams.keys():
		del teams[team_name]
		print("Team deleted")
	else:
		print("Wrong team name")

def manage_member_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
	print("\t\t4.Rename Team Name")
	print("\t\t5.Exit")
	
def add_member(team_name):
	display_employee()
	emp_id = int(input("Enter the emp_ID"))
	if emp_id in employee.keys():
		teams[team_name].append(emp_id)
	else:
		print("Invalid ID")

def delete_member(team_name):
	list_member((team_name))
	emp_id = int(input("Enter the emp_ID"))
	if emp_id in employee.keys():
		teams[team_name].remove(emp_id)
	else:
		print("Invalid ID")

def list_member(team_name):
	name_string = ""
	for i in teams[team_name]:
		name_string = name_string + employee[i]["emp_name"]
	print(f"{team_name} => {name_string}")
	
def rename_team(team_name):
	new_team_name = input("\t\tEnter new team name")
	lst = teams[team_name]
	del teams[team_name]
	teams[new_team_name] = lst
	
def manage_team_member():
	while True:
		display_teams()
		team_name = input("\t\tEnter team name ")
		manage_member_menu()
		ch = int(input("\t\tEnter the choice"))
		if ch == 1:
			#Add member
			add_member(team_name)
		elif ch == 2:
			#Delete member
			delete_member(team_name)
		elif ch == 3:
			#List member
			list_member(team_name)
		elif ch == 4:
			#Rename team
			rename_team(team_name)
		else:
			print("\tInvalid choice")
def manage_team():
	while True:
		manage_gpmenu()
		ch = input("\tEnter the choice")
		if ch == "a":
			#Create team
			create_team()
		elif ch == "b":
			#display teams
			display_teams()
		elif ch == "c":
			#Manage teams(Particular)
			manage_team_member()
		elif ch == "d":
			#Delete team
			delete_team()
		elif ch == "e":
			#exit
			break
		else:
			print("\tInvalid choice")	
def org_edit_menu():
	print("\t1. Edit Organisation name")	
	print("\t2. Edit email")	
	print("\t3. Edit phone number ")	
	print("\t4. Edit Website address")	
	print("\t5. Edit Organisation ID")
	print("\t6. Exit")	
	
def add_organisation():
	org_id = input("Enter Organisation ID")
	organisation[org_id] = {
			"name" : input("\tEnter Organisation name"),
			"email" : input("\tEnter email"),
			"phno" : input("\tEnter phone number"),
			"website" : input("\tEnter website")
		}
def org_name_change(org_id):
	new_name = input("\t\tEnter new Organisation name")
	organisation[org_id]["name"] = new_name

def org_email_change(org_id):
	new_email = input("\t\tEnter new Organisation email")
	organisation[org_id]["email"] = new_email

def org_phno_change(org_id):
	new_phno = input("\t\tEnter new Organisation phone number")
	organisation[org_id]["phno"] = new_phno

def org_website_change(org_id):
	new_website = input("\t\tEnter new Organisation website")
	organisation[org_id]["website"] = new_website

def view_organisation():
	for i,j in organisation.items():
		print(j)
		print(f"{i} => {j['name']} | {j['email']} | {j['phno']} | {j['website']}")
def edit_organisation():
	while True:
		org_edit_menu()
		org_id = input("\t\tEnter your organisation ID")
		ch = int(input("\t\tEnter the choice"))
		if ch == 1:
			org_name_change(org_id)
		elif ch == 2:
			org_email_change(org_id)
		elif ch == 3:
			org_phno_change(org_id)
		elif ch == 4:
			org_website_change(org_id)
		elif ch == 5:
			print("")
		elif ch == 6:
				break
		else:
			print("Invalid Choice")
while True : 
	menu()
	ch = int(input("Enter the choice"))
	if ch is None:
		print("Enter valid choice ")
	elif ch == 1:
		add_organisation()
	elif ch == 2:
		edit_organisation()
	elif ch == 3:
		view_organisation()
	elif ch == 4:
		add_employee()	
	elif ch == 5:
		delete_employee()
	elif ch == 6:
		search_employee_options()	
	elif ch == 7:
		update_empoyee()
	elif ch == 8:
		manage_team()	
	elif ch == 9:
		display_employee()
	elif ch == 10:
		break
	else:
		print("Invalid choice")
	
	
	
