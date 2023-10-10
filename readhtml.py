import pandas as pd
url = "http://cnm.casperlabs.io/network/casper/detail"

# print all rows rather than only head and tail
pd.set_option('display.max_rows', None)

content = pd.read_html(url)

df = content[0]
output = df.values.tolist()

count=0
for row in output:
    # print("0",row[0])
    # print("1",row[1])
    # print("2",row[2])
    # print("3",row[3])
    # print("4",row[4])
    # print("5",row[5])
    # print("6",row[6])
    # print("7",row[7])
    # print("8",row[8])
    # print("9",row[9])
    # print("10",row[10])
    # print("11",row[11])
    # print("12",row[12])
    # print("13",row[13])
    # print("14",row[14])
    # print("15",row[15])
    # print("16",row[16])
    # row[11] is upgrade era.  row[12] is weight%
    if (pd.isna(row[11])) and (not pd.isna(row[12])):
        # public key
        print(row[1])
        count+=1

print(count)
