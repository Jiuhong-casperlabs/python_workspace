import re
url = "/accounts/010a884bcada3e53f83e5fb80350e5ae325844dd49ba782ac16e4ef12cc41a11d0/deploys?page=1&limit=10"
digits_re=r'limit=.*'
output= re.sub(digits_re, 'limit=300', url, flags=re.IGNORECASE)
print(url)
print(output)

