class Shop:

    # as we know class attribut will be shared so we give here sth which can be used by the all instances
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
    def add_to_cart(self, item):
        self.cart.append(item)

mehzaabeen = Shop('mehzabeen is the buyer')
mehzaabeen.add_to_cart('shoe')
mehzaabeen.add_to_cart('phone')
print(mehzaabeen.cart)

nisho = Shop('he is nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

opurbo = Shop('i am opurba')
opurbo.add_to_cart('juta')
print(opurbo.cart)