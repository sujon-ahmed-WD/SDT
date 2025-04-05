# uniqe items collection . No duplicates
numbers =[12,56,98,56,5,5]
print(numbers)
numbers_set=set(numbers)
print(numbers_set)
 
if 9 in numbers_set:
 print('9 is exist')
elif 98 in numbers_set:
 print('98 is exist')