from abc import abstractmethod
from mars import Mars

class Rocket():
    def __init__(self,speed: int):
        self.speed = speed

    @abstractmethod
    def print_rocket_launch(self):
        pass

    @abstractmethod
    def launch_rocket(self) -> None:
        pass

    def calculate_time_to_mars(self) -> int:
        daysInSpace = 0
        
        distanceFromMars = Mars.abstract_distanceFromEarth()

        while(distanceFromMars > 0):
            distanceFromMars -= self.speed
            daysInSpace += 1

        return daysInSpace

   