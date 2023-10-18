# f = open("result1.json", "r")
# # print(f.read())

# for x in f:
#   deployhash=x
#   print(deployhash)

txt = "/accounts/012ba8401bb5a4b359b38cff86ce1002654406468e60787e11cec1c7d696be9185/deploys?page=1&limit=10"
a=txt.replace("limit=10", "limit=60")
print(txt)
print(a)