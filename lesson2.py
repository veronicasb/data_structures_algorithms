'''

METHOD

1. State the problem clearly and idenitfy output and inputs
2. Come up with example inputs and outputs and try to cover all edge cases
3. Come up with a correct solution in plain English
4. Implement the solution and test it using example inputs. Fix any bugs
5. Analyze the algorithm's complexity and identify inefficiencies
6. Apply the right techniques to overcome inefficiencies. Then, repeat steps 3-6

'''


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
'''
class User:
    # constructor method is essential
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        print(f"User {self.name} created!")

user1 = User("Kalin Denton", "Kalin", "bababa@gmail.com")
print(user1.name)
'''

# Add custom method to class
'''
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
'''

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
'''
class UserDatabase:
    def insert(self, user):
        pass
    
    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        pass

'''

###
# Step 2
###

# It's good practice to list out method signatures before implementation

valorie = User("Valorie Kuhens", "valorie", "vk@gmail.com")
jazmyne = User("Jazmyne Daniels", "jazmyne", "jd@gmail.com")
kalin = User("Kalin Denton", "kalin", "kd@gmail.com")
robin = User("Robin Sands", "robin", "rs@gmail.com")
monica = User("Monica Burgess", "monica", "mb@gmail.com")
lexi = User("Lexi Grant", "lexi", "lg@gmail.com")
jose = User("Jose Valasquez", "jose", "jv@gmail.com")

users = [valorie, jazmyne, kalin, robin, monica, lexi, jose]

'''

POTENTIAL SCENARIOS (for each operation)

1. Insert
- insert into an empty database
- insert a user with a username that already exists
- insert a user with a username that doesnt exist
- insert a user with an email that already exists

2. Find
- find a user by name
- find a user by username
- find a user by email
- find a user that does not exist

3. Update
- update a user's name
- update a user's username
- update a user's email
- update a user that does not exist

4. List All
- list all users by username
- list all users by name
- list all users by email
- list all from an empty database

'''


###
# Step 3
###

'''

SOLUTION IN PLAIN ENGLISH

We store User objects in a list sorted by usernames

The operations can be implemented:

1. Insert: loop through the sorted list of users, then add the new user at the postion
that keeps the list sorted

2. Find: Loop through the sorted of users, then find the user object with the username 
matching our query

3. Update: Loop through the sorted list, then find the user object matching the query 
and update the details

4. List: return the list of all User objects

- Note: strings can be compared like integers

'''


###
# Step 4
###

class UserDatabase:
    def __init__(self):
        # a call to this class takes no arguments
        # instantiating it will create an empty list for new users
        self.users = []

    def insert(self, user):
        # create a starting position at 0
        i = 0
        # iterate through all users
        while i < len(self.users):
            # Find the first username greater than the new user's username
            # letters that come before a letter are "less than"
            if self.users[i].username > user.username:
                # once we find the username that we must insert in front of, break out of while loop
                break
            # incrememt position by 1 until we find the username we must insert in front of
            i += 1
        # once we find the username that we must insert in front of, insert it
        self.users.insert(i, user)

    def find(self, username):
        # for each user in the users list...
        for user in self.users:
            # if the username we're looking for appears...
            if user.username == username:
                # return all associated information
                return user
            
    def update(self, user):
        # make a call to the find method, assign it to variables
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

# We can create a new database of users by instantiating an object of UserDatabase class
database1 = UserDatabase()

database1.insert(valorie)
database1.insert(jazmyne)
database1.insert(kalin)

database1.update(User(username = 'kalin', name = 'Kalin D', email = 'kalind@gmail.com'))

# Test potential scenarios

# inserts duplicate usernames
database1.insert(kalin)
print(database1.list_all())

# finds by username, returns None by other details and nonexistent users
print(database1.find('kalin'))
print(database1.find('Kalin D'))
print(database1.find('kalind@gmail.com'))
print(database1.find('veronica'))

# email didnt update, name updated, cant update username, updating a non existent user causes an error
database1.update(User(username='kalin', name='bababa', email='bababa@gmail.com'))
# database1.update(User(username='veronica', name='vero', email='vb@gmail.com'))
print(database1.list_all())


###
# Step 5
###

'''

Insert: O(N)
Find: O(N)
Update: O(N)
List: O(1)

We find that to iterate over 100 million users in our database with the structure we've created
so far, it would take about 10 seconds to simply list all the users, which is slow in today's
technology.

'''