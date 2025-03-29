# def full_name(first,last,nicname,username):
#     name=f'{first} {nicname} {last} {username}'
#     return name
# name=full_name('Alu','A','soki','moki')
# print(name)

def famous_name(first,last,**addition):
    name=f'{first} {last}'
    print(addition['mid'])
    return name
name=famous_name(first='s' , last='u', mid='j',end='on')
print(name)
# *args -> holo ata kaj sodu man golo return 
# **kargs-> akna key and value akra kaj korva 

