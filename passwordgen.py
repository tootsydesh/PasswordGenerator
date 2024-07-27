import random

lower_case = list(map(chr,range(97,123)))

upper_case = list(map(chr,range(65,91)))

lower_case.extend(upper_case)

numbers = list(map(int,range(0,10)))

characters = list(map(chr,range(33,42)))

Password = []
final_password =[]

length = int(input("What should be the lenght of your password?:\n"))
no_of_numbers = int(input("How many numbers do you want in your password?:\n"))
special_char = int(input("How many special characters do you want in your password?:\n"))


for i in range(1,no_of_numbers+1):
    chosen = str(random.choice(numbers))
    Password.append(chosen)

for i in range(1,special_char+1):
    chara = random.choice(characters)
    Password.append(chara)

for i in range(1,length-(no_of_numbers+special_char)+1):
    alpha = random.choice(lower_case)
    Password.append(alpha)


final_password = (random.sample(Password,length))

print("Your generated Password is: \n")
for i in range(0, length):
    print(final_password[i],end="")

    