numbers=[12,56,98,78,5]
# persion=['kala Chan',' kalipur',23,'student']
persion ={'name': 'kala pakhi','address':'kalipur','age':23,'job':'fasbook'}
print(persion.keys())
print(persion.values())
print(persion['address'])
persion['language']='bangla'
persion['name']='sada pakhi'
# del persion['age']
print(persion)
for key,value in persion.items():
    print(key,value)

