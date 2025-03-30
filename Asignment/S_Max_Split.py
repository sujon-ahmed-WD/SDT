val = input()   
l = 0
r = 0
balanced_substrings = []
temp = ""

for i in val:
    temp += i   
    if i == 'L':
        l += 1
    elif i == 'R':
        r += 1
    
    if l == r:  
        balanced_substrings.append(temp)   
        temp = ""   

 
print(len(balanced_substrings))   
for sub in balanced_substrings:
    print(sub)  #  

# val=input()
# l=0
# r=0
# for i in val:
#     if i=='L':
#         l+=1
#     if i=='R':
#      r-=1
# print(l,r) 