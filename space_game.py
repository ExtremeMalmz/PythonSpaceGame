from falcon import Falcon
from phobos import Phobos
from sputnik import Sputnik
from mars import Mars

class SpaceGame:
    def __init__(self):
        self.rocket = None
        self.start_game()
        
    def start_game(self) -> None:
        print("Welcome to the game\nYou will choose a rocket and once you have reached mars you will either plant a flag on its moon or start a lunar colony!")
        self.choose_rocket()

    def choose_rocket(self):
        choice = input("Sputnik (1) or Falcon (2)? ")

        match choice:
            case '1':
                self.rocket = Sputnik()
                self.rocket.launch_rocket()

            case '2':
                self.rocket = Falcon()
                self.rocket.launch_rocket()

        self.choose_colony_or_phobos()

    def choose_colony_or_phobos(self):
        mars = Mars()
        phobos = Phobos()

        print("\nYou've reached the red planet")

        print("Current colonies are:", end=' ')
        mars.print_colonies()

        print()
        print("The current flag holder of Phobos is: ", end='')
        phobos.print_flag_owner()

        print("\n\nTHANKS FOR PLAYING SPACE GAME")
