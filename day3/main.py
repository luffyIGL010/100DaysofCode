# conditional statements
# if, elif, else statements
# if condition:
    # do something
#  else:
    #  do something else
    
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age=int(input("What is your age? "))
# bill=0
# if height >=120:
#     if age < 12:
#         print("You can ride the rollercoaster!")
        
#         bill=5  
#         print(f"bill is ${bill}.")
        

#     elif age>=18:
#         print("You can ride the rollercoaster!")
#         #print("Please pay $12.")
#         bill=12
#         print(f"bill is ${bill}.")

        
#     else:
#         print("You can ride the rollercoaster!")
#         #print("Please pay $7.") 
#         bill=7
#         print(f"bill is ${bill}.")


        
#     input("Do you want a photo taken? Y or N.")
#     if input() == "Y":
#         bill+=3
        
#     print(f"bill is ${bill}.")     
# else:
#     print("Sorry ,you have to grow taller before you can ride.")
    
    
# num=int(input("Which number do you want to check? ")) 
# if num % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.") 



print("Welcome to Python Pizza deliveries!")
size = input("What size pizza do you want? S, M, or L? ")   
pepperoni = input("Do you want pepperoni? Y or N? ")    
extra_cheese = input("Do you want extra cheese? Y or N? ")  
bill=0
if size=="S":
    bill+=15
    if pepperoni=="Y":
        bill+=2
    if extra_cheese=="Y":
        bill+=1
elif size=="M":
    bill+=20
    if pepperoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
elif size=="L":         
    bill+=25
    if pepperoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
else:
    print("Please enter a valid size.")
print(f"Your final bill is: ${bill}.")
