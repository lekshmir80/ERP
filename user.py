#2.Create User class in erp.Employee class inherits the User class
#-Attributes of user(username,password,role)
#-Username and password are private variable
#3.When adding employee set his username and password also

class User:
	def __init__(self):
		self.__username = ""
		self.__password = ""
		self.role = ""
		
	def set_username(self,username):
		self.__username = username
	def get_username(self):
		return self.__username

	def set_password(self,password):
		self.__password = password
	def get_password(self):
		return self.__password
		
