import re
url = "/accounts/010a884bcada3e53f83e5fb80350e5ae325844dd49ba782ac16e4ef12cc41a11d0/deploys?page=9999&limit=10"
digits_re=r'page=\d+'
index = 3
output= re.sub(digits_re, f'page={index}', url, flags=re.IGNORECASE)
print(url)
print(output)

