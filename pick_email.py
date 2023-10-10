'''
pick emails from random content in file_pick_email.txt
'''
f = open("file_pick_email.txt").read().split()
# print(f)

filter_values = [x for x in f if "@" in x]

# [2*a for a in x if a % 2 == 1]
[print(x) for x in filter_values]
print(len(filter_values))