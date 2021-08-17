import employee as emp
teams = {}

def manage_member_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
	print("\t\t4.Rename Team Name")
	print("\t\t5.Exit")
	

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
def create_team():
	team_name = input("Enter the team name")
	teams[team_name] = []

def display_teams():
	for key,teamlist in teams.items():
		name_string = ""
		for i in teamlist:
			name_string = name_string + "|" +emp.employee[i]["emp_name"]
		print(f"{key} => {name_string}")

def delete_team():
	team_name = input("Enter the team name")
	if team_name in teams.keys():
		del teams[team_name]
		print("Team deleted")
	else:
		print("Wrong team name")
		
def add_member(team_name):
	emp.display_employee()
	emp_id = int(input("Enter the emp_ID"))
	if emp_id in emp.employee.keys():
		teams[team_name].append(emp_id)
	else:
		print("Invalid ID")

def delete_member(team_name):
	list_member((team_name))
	emp_id = int(input("Enter the emp_ID"))
	if emp_id in emp.employee.keys():
		teams[team_name].remove(emp_id)
	else:
		print("Invalid ID")
def list_member(team_name):
	name_string = ""
	for i in teams[team_name]:
		name_string = name_string + emp.employee[i]["emp_name"]
	print(f"{team_name} => {name_string}")
	
def rename_team(team_name):
	new_team_name = input("\t\tEnter new team name")
	lst = teams[team_name]
	del teams[team_name]
	teams[new_team_name] = lst
