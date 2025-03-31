# from collections import Counter

# # ইনপুট
# N = int(input())  # সিকোয়েন্সের দৈর্ঘ্য
# a = list(map(int, input().split()))  # সিকোয়েন্স

# # উপাদান গোনার জন্য Counter ব্যবহার করা
# count = Counter(a)

# # অপসারণের সংখ্যা
# remove_count = 0

# # প্রতিটি উপাদান চেক করা
# for key, val in count.items():
#     if key != val:  # যদি উপাদানটির সংখ্যা তার মানের সমান না হয়
#         remove_count += abs(val - key)  # যতটা পার্থক্য, ততটা বাদ দিতে হবে

# # আউটপুট
# print(remove_count)

from collections import Counter
N=int(input())
a=list(map(int,input().split()))

count=Counter(a)

remove_count=0

for key,val in count.items():
    if key!=val:
        remove_count+=abs(val-key)
print(remove_count)
