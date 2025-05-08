#randomization concept

import random
# import demo
# random_interger=random.randint(1,10)
# print(random_interger)

# print(demo.my_favourite_number)


# float_11=random.random() # returns a random float between 0.0 to 1.0
# print(float_11)

# uni_1=random.uniform(1,10) # returns a random float between 1.0 to 10.0 

# print(uni_1)    

#toss=random.choice(['Heads','Tails']) # returns a random element from the list

#print(toss)


#toss=random.randint(0,1)#
#if toss==0:
#    print('Heads')
# else:
#     print('Tails')
    
friends=['Alice','Bob','Charlie','David','Emanueal']
choice=random.choice(friends)
print(choice)
if choice=='Alice':
    print('Alice  will pays today bill  ')
    
elif choice=='Bob':
    print('Bob will pays today bill  ')             
    
elif choice=='Charlie':
    print('Charlie will pays today bill  ')     
    
    
elif choice=='David':               
    
    print('David will pays today bill  ')               
    
    
elif choice=='Emanueal':
    print('Emanueal will pays today bill  ')
    
    
else:
    print("No will pays today bill ")