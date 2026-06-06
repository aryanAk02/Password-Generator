import random

print("\nWELCOME TO PASSWORD GENERATOR\n")

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']

pw_letters=int(input("How many letters you want in password?\n"))
pw_numbers=int(input("How many numbers you want in password?\n"))
pw_symbols=int(input("How many symbols you want in password?\n"))


#medium level
# password=""
# for i in range(0,pw_letters):
#     password+=random.choice(letters)

# for i in range(0,pw_numbers):
#     password+=random.choice(numbers)

# for i in range(0,pw_symbols):
#     password+=random.choice(symbols)

# print("password is :"+password)

#hard level

password_list=[]

for i in range(0,pw_letters):
    password_list.append(random.choice(letters))
for i in range(0,pw_numbers):
    password_list.append(random.choice(numbers))
for i in range(0,pw_symbols):
    password_list.append(random.choice(symbols))

#method1
# print(password_list)
# password=""
# for i in password_list:
#     password+=random.choice(password_list)

# print(password)

#method2

password=""

print(password_list)
random.shuffle(password_list)
print(password_list)

for i in password_list:
    password+=i

print(password)