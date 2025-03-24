def sum(num1,num2,num3=0):
    result=num1+num2+num3
    return result
total=sum(5,5)
print(total)
# args
# def all_sum(num1,num2,*numbers):
#     sum=0
#     print(numbers)
#     for num in numbers:
#         print(num)
#         sum+=num
#     return sum
 
# total=all_sum(5,10,15,20)
# print('all sum:',total) 
def all_sum(*numbers):
    sum=0
    print(numbers)
    for num in numbers:
        print(num)
        sum+=num
    return sum
total=all_sum(5,10,15,20)
print('all sum :',total)     