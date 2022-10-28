from rocket import Rocket

class Falcon(Rocket):
    def __init__(self):
        self.__name = "Falcon"
        self.__speed = 10
        super().__init__(self.__speed)

    def print_rocket_name(self):
        print("Hello I am a falcon!")
        print("Three \nTwo \nOne")

    def launch_rocket(self):
        self.print_rocket_name()
        print("Falcon has landed on mars after " + str(self.calculate_time_to_mars()) + " days of travel!")
        print("Thank you for flying a " + self.__name)