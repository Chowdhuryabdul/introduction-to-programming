class Pen:
    def __init__(self, brand, owner, price):
        self.brand = brand
        self.owner = owner
        self.price = price

my_pen = Pen('econo', 'you', 4000)
print(my_pen.brand, my_pen.owner, my_pen.price)

her_pen = Pen('dx', 'she', 600)
print(her_pen.price, her_pen.owner, her_pen.brand)
