from abc import ABC, abstractmethod

class Iguana(ABC):
    SPECIES_NAME = "Iguana"
    __instances = []

    def __init__(self, age: int) -> None:
        self.age = age
        Iguana.__instances.append(self)

    @classmethod
    def how_many_iguanas(cls) -> int:
        return len(cls.__instances)

    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def sleep(self) -> None:
        pass

    @classmethod
    def count_iguanas(cls) -> dict:
        return {cls.__name__: len(cls.__instances)}
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} (Age: {self.age})"
    
class GreenIguana(Iguana):
    SPECIES_NAME = "Green Iguana"

    def eat(self) -> None:
        print(f"The {self.SPECIES_NAME} is eating")
    
    def sleep(self) -> None:
        print(f"The {self.SPECIES_NAME} is sleeping")

    def __str__(self) -> str:
        return f"{self.SPECIES_NAME} (Age: {self.age})"
    
class SpinyIguana(Iguana):
    SPECIES_NAME = "Spiny Iguana"

    def eat(self) -> None:
        print(f"The {self.SPECIES_NAME} is eating")
    
    def sleep(self) -> None:
        print(f"The {self.SPECIES_NAME} is sleeping")

    def __str__(self) -> str:
        return f"{self.SPECIES_NAME} (Age: {self.age})"
    
if __name__ == "__main__":
    green_iguana1 = GreenIguana(3)
    green_iguana2 = GreenIguana(5)

    spiny_iguana1 = SpinyIguana(2)
    spiny_iguana2 = SpinyIguana(4)


    green_iguana1.eat()
    green_iguana2.sleep()

    spiny_iguana1.sleep()
    spiny_iguana2.eat()

    print(green_iguana1)
    print(spiny_iguana1) 


    for iguana_type, count in Iguana.count_iguanas().items():
        print(f"{iguana_type}: {count}")