import random

def deal_card():
    """Return a random card from the list of cards."""
    cartes = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cartes)

# Function to calculate scores
def calculate_score(cards):
    # Check for a natural blackjack (21 with only two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Adjust for Aces (11 -> 1) if the sum is over 21
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

# Function to compare scores and determine the result
def compare(userscore, computerscore):
    if userscore == computerscore:
        return "It's a Draw."
    elif computerscore == 0:
        return "You Lose! Computer has a Blackjack."
    elif userscore == 0:
        return "You Win with a Blackjack!"
    elif userscore > 21:
        return "You went over 21! You Lose."
    elif computerscore > 21:
        return "Computer went over 21! You Win!"
    elif userscore > computerscore:
        return "You Win!"
    else:
        return "You Lose."

# Main function to play a game of Blackjack
def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards to both player and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Game loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'yes' to get another card or 'no' to pass:\n").lower()
            if user_should_deal == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Loop to allow replaying the game
while input("Play Blackjack? Type 'yes' to play or anything else to exit: ").lower() == 'yes':
    play_blackjack()
    print("\n" * 2)  # Adds some spacing between game sessions
