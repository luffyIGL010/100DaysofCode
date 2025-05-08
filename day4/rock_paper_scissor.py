
import random
#Wlecome to rock paper scissor game
print("Welcome to Rock Paper Scissor Game")

input=['Rock','paper','Scissors']
user_input=random.choice(input)
computer_input=random.choice(input) 


if user_input==computer_input:
    print("It's a Tie")
elif user_input=='Rock' and computer_input=='Scissors':     
    print("You win")
elif user_input=='Rock' and computer_input=='paper':
    print("Computer win")       
elif user_input=='paper' and computer_input=='Rock':
    print("You win")
elif user_input=='paper' and computer_input=='Scissors':
    print("Computer win")
elif user_input=='Scissors' and computer_input=='Rock':
    print('Computer win')
    
elif user_input=='Scissors' and computer_input=='paper':
    print("You win ")
    
else:
    print("This is not a valid input")  
    
    
    
#lsit comprehension     
squares=[x**3 for x in range(8)]

print(squares)

table_2=[2*i for i in range(1,11)]
print(table_2) 