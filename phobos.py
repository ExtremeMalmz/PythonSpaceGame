class Phobos:
    def __init__(self):
        self.__flagHolder = "Martians"

    def change_flag_owner(self, newFlagOwner: str) -> None:
        self.__flagHolder = newFlagOwner

    def print_flag_owner(self) -> None:
        print("Phobos Flag holder is currently: " + self.__flagHolder)
