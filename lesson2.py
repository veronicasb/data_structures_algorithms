'''

PROBLEM

Develop a fast in-memory data structure to manage profile information (username, name, email) for 100 
million users. It should allow the following operations to be performed:
- Insert profile information for a new user
- Find profile information of a user with their username
- Update profile information of user with their username
- List all users of the platform sorted by username

You can assume all usernames are unique

'''

'''

METHOD

1. State the problem clearly and idenitfy output and inputs
2. Come up with example inputs and outputs and try to cover all edge cases
3. Come up with a correct solution in plain English
4. Implement the solution and test it using example inputs. Fix any bugs
5. Analyze the algorithm's complexity and identify inefficiencies
6. Apply the right techniques to overcome inefficiencies. Then, repeat steps 3-6

'''

###
# Step 1
### 

'''
We need to create a data structure that can store 100 million records and perform
insertion, search, update, and list operations efficiently.

A data structure is something we can define using a class.

INPUTS
details to create a new user:
- user profiles (username, name, email)

OUTPUTS
details from doing the following operations:
- insert
- find
- update
- list_all

'''

# OOP
# classes are a perfect way to represent a person of some kind
# a class is a blueprint for creating an object
class User:
    pass

user1 = User()
print(type(user1))


# Add constructor method to classes to store attributes or properties
# Constructor methods are special funtions that create an instance of a class.
class User:
    # constructor method is essential
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        print(f"User {self.name} created!")

user1 = User("Kalin Denton", "Kalin", "bababa@gmail.com")
print(user1.name)


# Add custom method to class
class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        print(f"User {self.name} created!")

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}.")

user2 = User("Shiela Socorro", "Shiela", "radarada@gmail.com")
user2.introduce_yourself("Kalin")


# remove any print statements and add helper methods
# these methods are used to create a string representation of our object
class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User (username = '{self.username}', name = '{self.name}', email= '{self.username}')"
    
    def __str__(self):
        return self.__repr__()
    
'''
__str__() and __repr__()

These 2 functions return an objects string representation.

They're different in that __repr__() is intended to hold information about the object so that it may be created again.
__repr__() is a developer-friendly string representation of an object, while 
__str__() is more human/user-friendly and used for logging reasons.

'''

# Create a class for our output
class UserDatabase:
    def insert(self, user):
        pass
    
    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        pass

# It's good practice to list out method signatures before implementation