from data import data1
import random
user1=random.choice(data1)
user2=random.choice(data1)
print(user1)
print(user2)
score=0
game_over=False
while not game_over:
    if user1==user2:
       user2=random.choice(data1)
    print(f"Compare A: {user1['name']}, a {user1['description']}, from {user1['country']}.")
    print("VS") 
    print(f"Against B: {user2['name']}, a {user2['description']}, from {user2['country']}.")
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice=="a":
        if user1['follower_count']>user2['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}.")
            user1=user2
            user2=random.choice(data1)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over=True
    elif choice=="b":
        if user2['follower_count']>user1['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}.")
            user2=user1
            user1=random.choice(data1)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over=True
    else:
        print("Invalid input. Please enter 'A' or 'B'.")
        continue
    