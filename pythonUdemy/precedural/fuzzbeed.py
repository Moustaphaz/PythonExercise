import string
import random

list_of_letter =list(string.ascii_letters)
list_of_numbers =[str(i) for i in range(0,10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters =int(input("donner le nombre de lettres : \n"))
number_of_numerics =int(input("donner le nombre de chiffres :\n"))
number_of_symbols =int(input("donner le nombre de symbols :\n"))

password =[]

#print(list_of_numbers)

password += random.choices(list_of_letter,number_of_letters)
print(password)
password +=random.sample(list_of_numbers,number_of_numerics)
password += random.sample(symbols,number_of_symbols)

random.shuffle(password)

final_pwd =''.join(password)

print("votre mot de passe est :", final_pwd)

