# your improved User class goes here
from datetime import datetime

class Users():
    all_posts = []
    last_post = None
    
    def __init__(self, first, last, phone, address) -> None:
        self.first = first
        self.last = last
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        return f"""
        user:       {self.fullname}
        email:      {self.email}
        phone:      {self.phone}
        address:    {self.address}
        """

    @property   # Property tag allows method to be called like an attribute
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}" + "@email.com"

    @property   # Property tag allows method to be called like an attribute
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    @fullname.setter    # Setter allows class to automatically update attributes as properties change
    def fullname(self, name) -> str:
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def post(self, post) -> str:
        if(Users.last_post == self.fullname):
            Users.all_posts.append([self.fullname, post, f'{datetime.now().strftime("%m/%d/%Y")}', f'{datetime.now().strftime("%H:%M:%S")}'])
            return f""" > {post}"""
        else:
            Users.all_posts.append([self.fullname, post, f'{datetime.now().strftime("%m/%d/%Y")}', f'{datetime.now().strftime("%H:%M:%S")}'])
            Users.last_post = self.fullname
            return f"""{self.fullname}:\n > {post}"""

    @staticmethod
    def post_history() -> None:
        print("\nPost History:")
        for posts in Users.all_posts:
            print(posts)
         
# Instantiate users 1 and 2
user_1 = Users('John', 'Doe', '123-456-7890', '123 Main St')
user_2 = Users('Jane', 'Doe', '098-765-4321', '456 Grand Blvd')

# Display their properties
print(f"User 1: {user_1}")
print(f"User 2: {user_2}")

print(user_1.post('Test'))
print(user_1.post('Good Morning'))
print(user_2.post('Hi John!'))
print(user_1.post('Hello Jane!'))

Users.post_history()