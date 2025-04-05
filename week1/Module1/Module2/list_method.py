number =[10,25,50]
number.append(11)
print(number)
number.insert(2,55)
print(number)
if 10 in number:
    number.remove(10)
    print(number)
if 5 in number:
    number.insert(0)
    print(number)
last =number.pop()
print('last num',number)
 
    