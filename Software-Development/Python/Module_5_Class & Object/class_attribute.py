# To show the difference btween class attribute and constructor attribute
class Shop:
    # making attribut of the class
    cart = [] #it is called calss attribute if it is not declared inside the method
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)
mehzabeen = Shop('meh zabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart) #here after printing we have got the mehazabeen things in the cart of Nisho. why this is becuase we have taken a class_attribute. this class attribute will be shared, it menas all the instance will use this attribute. so if make several instances, so next instance will get the value which is given to the previous instance, althoug the instance is difference. as we see here nisho has got the mehzabeen things. so when we declare the class attribute we have to notice that will this attribute will be connected to the instance or something else.