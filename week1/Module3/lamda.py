# def fun(x):
#     return x*2
# result=fun(2)
# print(result)
double=lambda x:x*2
result=double(2)
print(result)
numbers=[12,56,98,78,56,12,6,98]
double_nums=map(double,numbers)
print(list(double_nums))
actors=[
    {'name':'s','age':65},
    {'name':'j','age':30},
    {'name':'u','age':45},
    {'name':'o','age':38},
]
jounor=filter(lambda actor:actor['age']<40,actors)
print(list(jounor))