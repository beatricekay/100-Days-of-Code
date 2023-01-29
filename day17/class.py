# Creating a class
class User:
    
    # Whenever a new object is created from this class, it must provide 2 pieces of information in the ()
    def __init__(self, id, username):
        # Creating attributes
        self.id = id
        self.username = username
        self.followers = 0 # Since this value is defined, it doesn't have to be specified when creating the object
        self.following = 0
        print("new user being created...") 
    
    # A method always needs to have a self parameter as the first parameter
    # This means that when the method is called, it's referencing the object that called it
    def follow(self, user):
        # When we follow a user, its follower count increases by 1 while our following count increases by 1 as well
        # self refers to the object itself 
        user.followers += 1
        self.following += 1
    
    # Python doesn't allow objects to be defined when there is no content in the class
    # Typing 'pass' allows you to overcome this error
    # pass

# Creating object user_1
user_1 = User("001", "angela")
# 1) Manually assigning attributes to an object
user_1.id = "001"
user_1.username = "angela"

# 2) Assigning an attribute to an object through the class (both methods are acceptable)
# We specify the attribute value when creating the class. Make sure the attribute is added as a parameter in the __init__ function
# Creating object user_2
user_2 = User("002", "beatrice")
print(user_2.id)
print(user_2.username)
print(user_2.followers)

# Using created method follow()
user_1.follow(user_2) # user_1 follows user_2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
