class phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    # it is called method - you need to give here other parameter, but if you do not give other parameter than you have to put self as parameter
    # this method - it refers to a function which is added inside the class
    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms): #here first number should show as parameter, but it shows the second one as parameter and consider first one as instance. so that is why people uses self as instance, than it will show all others parameters. after adding defalut self, now it will show others two parameters
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(40577963, 'i forgot to miss you')
print(result)

# when you make a object from a class it will automatically make instance 