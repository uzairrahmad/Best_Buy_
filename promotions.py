from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        """
        This method is a concrete method of abstract class.It takes two self.price as product
        and quantity by user,apply promotions and return the total
        """
        final_total = 0
        for number in range(1, quantity + 1):
            if number % 2 == 0:
                final_total += product * 0.5
            else:
                final_total += product
        return final_total


class ThirdOneFree(Promotion):
    """
    This method is a concrete method of abstract class.It takes two self.price as product
    and quantity by user,apply promotions and return the total
    """

    def apply_promotion(self, product, quantity):
        final_total = 0
        for number in range(1, quantity + 1):
            if number % 3 == 0:
                final_total += product * 0
            else:
                final_total += product * 1
        return final_total


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
          This method is a concrete method of abstract class.It takes two self.price as product
          and quantity by user,apply promotions and return the total
          """
        return product * quantity - (product * quantity * self.percent / 100)
