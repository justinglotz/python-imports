from appliances.appliance import Appliance

class CoffeeMaker(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def make_coffee(self):  # Added self
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
