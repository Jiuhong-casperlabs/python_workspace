# f=open("from_work3_ouput.txt", "r")

# for x in f:
#     print(x)

with open('input2.txt', 'r') as f:
   lines = f.readlines()
   for line in lines:
       if "arg_delegator" in line:
          print(line.split()[1])
     
