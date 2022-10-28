from rocket import Rocket

class Sputnik(Rocket):
    def __init__(self):
        self.__name = "Sputnik"
        self.__speed = 5
        super().__init__(self.__speed)

    def print_rocket_name(self):
        print("привет Я спутник!")
        print("ТРИ \nДBA \nOДИH")

    def launch_rocket(self):
        self.print_rocket_name()
        print("We have arrived on MAPC after " + str(self.calculate_time_to_mars()) + " days of travel!")
        print("Thank you for choosing a " + self.__name)