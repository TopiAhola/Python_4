
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name} serves wonderful {self.cuisine_type}. ')

    def open_restaurant(self):
        print(f'{self.name} is open. Come on in!')










#main
if __name__ == '__main__':
    restaurant = Restaurant('Kotipizza', 'pizza')
    print(restaurant.name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()