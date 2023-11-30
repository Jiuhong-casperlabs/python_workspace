with open("string.txt","r") as f:
    emails = f.read().split(":")
    print(len(emails))

[print(email) for email in emails]

