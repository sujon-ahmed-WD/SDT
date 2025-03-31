
# t = int(input())   
# count = 0

# for i in range(t):   
#     values = list(map(int, input().split()))  # Input for each test case
#     operation_count = 0  # প্রতিটি টেস্ট কেসের জন্য নতুন কাউন্ট

#     # যতক্ষণ পর্যন্ত সব সংখ্যা জোড় থাকবে, 2 দিয়ে ভাগ করা হবে
#     while all(x % 2 == 0 for x in values):  
#         values = [x // 2 for x in values]  # সবাইকে 2 দিয়ে ভাগ করা হবে
#         operation_count += 1  # অপারেশন গুনে বাড়ানো হবে

#     print(operation_count)  # প্রতিটি টেস্ট কেসের জন্য আউটপুট প্রিন্ট করবো

#---------------------
N = int(input()) 
values = list(map(int, input().split()))  
count = 0 
while all(x % 2 == 0 for x in values):  # akna holo amier vallue even asa ke nh
   values = [x // 2 for x in values]   # ja ja man golo even asa oigolo ami mobag korbo
   count += 1  
print(count)

"""
Qustion balo kora Clear 
logic ta holo amier man golo ke jor asa ke na and sa golo ka ami bag kora count korbo ........
"""  
 
        
         
        
        
 
    
   