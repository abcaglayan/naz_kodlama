# istenilen kahve listede var mı ok
# varsa süt tercihi sor
# yoksa bir daha input alsın(forever) ok


import time

def coffe_order():
    price = 0
    name = input("What is your name for order? ")
    order = input("Put order... ")
    while order != 'yeter':
        order = input("Put order... ")
        coffe_types = {"mocca": {'price': 12,'milk': True}, "tea": {'price':15,'milk':False},"water": {'price':20,'milk':False},"latte": {'price':30,'milk':True}, "matcha": {'price':26,'milk':True}, "spanish latte": {'price':29,'milk':True} }
        while order not in coffe_types:
            print("Sorry, coffe order was not recognized")
            order= input("Put another order")
        print(f"Your coffe order is: {order}, price is {coffe_types[order]['price']}")
        if coffe_types[order]['milk'] == True:
            print("You need to choose also milk")
        price += coffe_types[order]["price"]

        if coffe_types[order]["milk"] == True:
            milk= input("Put milk preferance: ")
            milk_types = {"lactosefree": 5, "almondmilk": 8, "oatmilk": 3}
            while milk not in milk_types:
                print("Sorry, milk preferance was not recognized")
                milk= input("Put another milk preferance")
            print (f"you chose {milk}, price is {milk_types[milk]}")
            price += milk_types[milk]
        print(f"Your total price is: {price}")

    time.sleep(10)
    print(f"Your order is ready mr/mrs {name} ")

coffe_order()


# assowrd check
password = 'XYZabcdef1234!'

def check_password(password):
    is_valid = False
    len_p = len(password)
    # length
    if len_p > 8:
        is_valid = True
    else:
        print("invalid password")
        return False
    # sonda ünlem var mı
    if password[-1] == '!':
        return False

    # capital
    for letter in password:
        if letter == letter.capitalize():
            is_valid = True
    if is_valid == False:
        return False

    # capital
    for letter in password:
        if letter == letter.capitalize():
            is_valid = True
    if is_valid == False:
        return False








