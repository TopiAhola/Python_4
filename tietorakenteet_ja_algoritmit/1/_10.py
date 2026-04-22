class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f'''Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail: {self.email}\nLocation: {self.location}''')

    def greet_user(self):
        print(f"Welcome back {self.username}!")



#main

Matti = User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
Matti.describe_user()

Maila = User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
Maila.greet_user()

Pekka = User('Pekka', 'Seppänen', 'pseppanen', 'p.Seppanen@yle.fi', 'Espoo')
Pekka.describe_user()
Pekka.greet_user()