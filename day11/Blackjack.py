cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)



player_cards=[deal_card(),deal_card()]
computer_cards=[deal_card(),deal_card()]


# Calculate the score of the cards
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

game_over=False

# Game_Loop
while not game_over:
    player_score=calculate_score(player_cards)
    computer_score=calculate_score(computer_cards)
    print(f"   Your cards: {player_cards}, current score: {player_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if player_score==0 or computer_score==0 or player_score>21:
        game_over=True
    else:
        should_continue=input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue=="y":
            player_cards.append(deal_card())
        else:
            game_over=True
            
# Computer's turn            
while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
print(f"   Your final hand: {player_cards}, final score: {player_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

# Compare scores

if player_score>21:
    print("You went over. You lose!")
elif computer_score>21:
    print("Computer went over. You win!")
elif player_score==computer_score:
    print("Draw")
elif player_score==0:
    print("Blackjack! You win!")
elif computer_score==0:
    print("Computer got blackjack. You lose!")
elif player_score>computer_score:
    print("You win!")
else:
    print("You lose!")  
    
    
    
# This code is a simple implementation of the Blackjack game. It allows a player to play against a computer dealer, dealing cards and calculating scores based on the rules of Blackjack.
    