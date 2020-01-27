"""The Acme Report."""

from random import randint, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Create a list of randomized sample ACME products."""
    products = []

    for _ in range(num_products):
        name = choice(ADJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name,
                                price=price,
                                weight=weight,
                                flammability=flammability))

    return products


def inventory_report(products):
    """Generate a report from the products."""
    # Length of product list
    list_length = len(products)

    total_price = 0
    total_weight = 0
    total_flammability = 0

    for product in products:
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    avg_price = total_price / list_length
    avg_weight = total_weight / list_length
    avg_flam = total_flammability / list_length

    print("ACME CORPORATION OFFICAL INVENTORY REPORT")
    print("Unique product names:", list_length)
    print("Average price:", avg_price)
    print("Average weight", avg_weight)
    print("Average flammability:", avg_flam)


if __name__ == '__main__':
    inventory_report(generate_products())
