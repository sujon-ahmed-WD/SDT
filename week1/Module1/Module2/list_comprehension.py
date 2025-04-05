number=[45,47,96,65,43,90,85,14]
odds=[]
for num in number:
    if num%2==1 and num%5==0:
        odds.append(num)
print(odds)
odd_nums=[num for num in number if num%2==1 if num%5==0]
print(odd_nums)