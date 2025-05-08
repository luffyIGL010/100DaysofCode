# Welcome to password generator game :
import random
print("Welcome to password generator game:")

student_scores=[21,34,64,98,11,122,45]
symbol=['*','&','$','#',]

length_letters=int(input("Enter the length of strings:"))
symbols_length=int(input("Enter the length of the symbols"))
password=[]


#letter_password=random.choices(student_scores,k=length_letters)

#symbol_password=random.choices(symbol,k=symbols_length)



#Choice_password=letter_password+symbol_password
#random.shuffle(Choice_password)

#print(Choice_password)


# i did without using for loop and list comprehension



for _ in range(length_letters):
    password.append(random.choice(student_scores))
        
        
for _ in range(symbols_length):
    password.append(random.choice(symbol))
    
    
pasword=random.shuffle(password)
print(password)
    
