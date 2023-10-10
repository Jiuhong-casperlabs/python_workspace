import requests
url = "http://cnm.casperlabs.io/network/casper/detail"

r=requests.get(url)
file = r.text
x = file.split("<table")
y=x[1]
z=y.split("</table>")
values = z[0]

rows = values.split("<tr>")


# print("row-0",rows[0])

# print("row-2",rows[2])  # start here
# print("row-3",rows[3])
# print("row-last",rows[len(rows)-1])

count =0
for x in range(2, len(rows)):
    td_values = rows[x].split("<td>")
    # print(td_values[0],td_values[1])
    # print("values[0]",td_values[0].strip().strip("</td>"))
    # print("values[1]",td_values[1].strip().strip("</td>"))
    # print("values[2]",td_values[2].strip().strip("</td>"))
    # print("values[3]",td_values[3].strip().strip("</td>"))
    # print("values[4]",td_values[4].strip().strip("</td>"))
    # print("values[5]",td_values[5].strip().strip("</td>"))
    # print("values[6]",td_values[6].strip().strip("</td>"))
    # print("values[7]",td_values[7].strip().strip("</td>"))
    # print("values[8]",td_values[8].strip().strip("</td>"))
    # print("values[9]",td_values[9].strip().strip("</td>"))
    # print("values[10]",td_values[10].strip().strip("</td>"))
    # print("values[11]",td_values[11].strip().strip("</td>"))
    # print("values[12]",td_values[12].strip().strip("</td>"))
    # print("values[13]",td_values[13].strip().strip("</td>"))
    if len(td_values[12].strip().strip("</td>"))== 0:
        if  not len(td_values[13].strip().strip("</td>"))==0:  #ok

            count +=1
            print(td_values[2].strip().strip("</td>"))
            print(td_values[1].strip().strip("</td>"),)

print("count:",count)


print("row-1",rows[1])

