# Part 1 Keeping it Classy.

from random import randint


class Product:
    """Products of the Company."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Initialize properties of the class."""
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

# Part 2 - Objects that Go!

    def stealability(self):
        """How Stealable is this product?."""
        priceweight = (self.price / self.weight)
        if priceweight < 0.5:
            return "Not so stealable..."
        elif priceweight >= 0.5 and priceweight < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Is this thing gonna blow up?."""
        flameweight = (self.flammability * self.weight)
        if flameweight < 10:
            return "...fizzle"
        elif flameweight >= 10 and flameweight < 50:
            return "...boom!"
        else:
            return "...BABOOOM!!"

# Part 3 - A Proper Inheritance


class BoxingGlove(Product):
    """A Boxing Glove that gets inheritance from Product."""

    def __init__(self, name):
        """Initialize boxingglove subclass."""
        super().__init__(name, weight=10)

    def explode(self):
        """Cannot explode therefore overridden."""
        return "...it's a glove."

    def punch(self):
        """For punching."""
        if self.weight < 5:
            return "That tickles.."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
