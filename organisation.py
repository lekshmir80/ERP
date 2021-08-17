organisation = {}
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
