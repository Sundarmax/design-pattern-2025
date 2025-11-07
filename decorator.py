from abc import ABC,abstractmethod

# component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# concrete componenent
class SimpleCoffee(Coffee):
    def cost(self):
        return 10

# decorator
class CoffeeDecorator(Coffee):

    def __init__(self, coffee):
        self._coffee = coffee
    
    @abstractmethod
    def cost(self):
        pass

# concrete decorator
class MilkDecorator(CoffeeDecorator):
    
    def cost(self):
        return self._coffee.cost() + 5

class SugarDecorator(CoffeeDecorator):
    
    def cost(self):
        return self._coffee.cost() + 2

if __name__ == "__main__":
    simple_coff = SimpleCoffee()
    print(simple_coff.cost())
    coffee_with_milk = MilkDecorator(simple_coff)
    print(coffee_with_milk.cost())
    coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
    print(coffee_with_milk_sugar.cost())
