# f=open("from_work3_ouput.txt", "r")

# for x in f:
#     print(x)

count = 0
with open('from_work3_ouput.txt', 'r') as f:
   lines = f.read().split('========================')
   for line in lines:
    #   print(line)
      
      for x in line.split("\n"):
        if "TO SEE:" in x:
            count += 1
            print(line)

print(count)
