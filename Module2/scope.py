# balance=3000
# def buy_thing(item,price):
#      global balance
#      balance=balance-price
#      print("afther balace ")
# name=buy_thing('sungalss',100)
# print(name)
balance =3000
def buy_thing (item,price):
    global balance
    balance=balance-price
    return balance
name=buy_thing('s',200)
print(name)