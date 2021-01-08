email_address = input("Please enter your email address: ").strip()

username = email_address[:email_address.index("@")]

domain = email_address[email_address.index("@")+1:]

statement = "Your username is '{}' and your domain  is '{}'".format(username,domain)

print(statement)
