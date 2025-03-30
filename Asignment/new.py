val=input()
l=0
r=0
balans_sting=[]
tmp=""
for i in val:
    tmp+=i
    if i=='L':
        l+=1
    if i=='R':
     r+=1
    if l==r:
        balans_sting.append(tmp)
        tmp=""
print(len(balans_sting))
for sub in balans_sting:
    print(sub)

#qusion nh buja 
# sub string logic golo bujer dorker chllo array dea push kora 