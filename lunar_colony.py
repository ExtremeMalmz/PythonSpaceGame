class LunarColony:
    def __init__(self, name, founder):
        self.__colonyName = name
        self.__foundingCountry = founder

    def __str__(self) -> str:
        return self.__colonyName + " founded by " + self.__foundingCountry