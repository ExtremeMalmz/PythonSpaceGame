from abc import abstractmethod
from lunar_colony import LunarColony
from phobos import Phobos

class Mars:
    def __init__(self):
        self.__distanceFromEarth = 100
        self.listOfColonies = [LunarColony("Base 1", "America"), LunarColony("Base Alexander", "Russia")]

    def get_distanceFromEarth(self):
        return self.__distanceFromEarth

    @abstractmethod
    def abstract_distanceFromEarth():
        return 100

    def print_colonies(self):
        for i in self.listOfColonies:
            print(i, end=' - ')
