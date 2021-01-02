email = input('Enter Your Email:- ')

# slice out the user_name
user_name = email[:email.index('@')]

print(user_name)

# slice the domain name
domain_name = email[email.index('@')+1:]

print(domain_name)

#format msg

output = "Your Username :--'{}' and Your Domain name:-- '{}' ".format(user_name,domain_name)

#display msg
print(output)