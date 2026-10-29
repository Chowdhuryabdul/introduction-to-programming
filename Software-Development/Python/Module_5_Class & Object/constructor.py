class Phone:
    manufactureds = 'china' # it is called attribute of class


    # methods
    def send_sms(self, phone, sms):
        text = f'sending to: {phone}{sms}'
        print(text)

    # there are lot of methods i can use in the class - i will write def than two inderscore than it will show those automatically
    # my goal is to make many object from this phone class and all the phones will have self features. it means i will give seperate features 

    def __init__(self, owner,  brand, price): # another language it gives as constructor, but in python it gives as initialize or init. it is actually constructor
       # pass # pass means it is empty i will not do anything here
       self.owner = owner # when we send the value of parameter owner. it will be set in the self.owner attribute.
       self.brand  = brand  # self.brand - this part is name of the attribute = brand this part is value of attribute
       self.price = price

    #    why we give it to the self? - self.price = price. when you make object from the class 

# objec of this class
# instance is the made object from class
my_phone = Phone('Kala Chan', 'Oppo', 9800)
print(my_phone.owner, my_phone.brand, my_phone.price)
her_phone = Phone('Rahim', 'NNokia', 3400)
print(her_phone.owner, her_phone.price, her_phone.brand)