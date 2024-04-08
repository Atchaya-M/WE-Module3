import random

def initialize_deck():
    suits = ['Hearts', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    players = {
        'Player': [],
        'Computer': []
    }
    for _ in range(13):
        players['Player'].append(deck.pop())
        players['Computer'].append(deck.pop())
    return players

def initialize_diamond_cards():
    diamond_cards = [
        ('Ace', 'Diamonds'),
        ('2', 'Diamonds'),
        ('3', 'Diamonds'),
        ('4', 'Diamonds'),
        ('5', 'Diamonds'),
        ('6', 'Diamonds'),
        ('7', 'Diamonds'),
        ('8', 'Diamonds'),
        ('9', 'Diamonds'),
        ('10', 'Diamonds'),
        ('Jack', 'Diamonds'),
        ('Queen', 'Diamonds'),
        ('King', 'Diamonds')
    ]
    return diamond_cards

def get_rank_value(rank):
    rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
        'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
    }
    return rank_values.get(rank, 0)  

def get_computer_bid(diamond, computer_hand, used_cards, num_cards_remaining, computer_used_cards):
    diamond_value = get_rank_value(diamond[0])
    
    THRESHOLD = 4
    
    if diamond_value >= 10 or (num_cards_remaining <= THRESHOLD and len(computer_hand) > 1):
        for card in computer_hand:
            if card not in used_cards and card not in computer_used_cards and get_rank_value(card[0]) >= 8:
                return card
    elif diamond_value < 8:
        for card in computer_hand:
            if card not in used_cards and card not in computer_used_cards and get_rank_value(card[0]) <= 6:
                return card
    
    available_cards = [card for card in computer_hand if card not in used_cards and card not in computer_used_cards]
    return random.choice(available_cards)

def conduct_auction(diamond_card, player_cards, computer_cards, diamond_cards):
    print("\nDiamond Card to be bid:", format_card(diamond_card))
    print("Your cards for this round:")
    print_cards(player_cards)
    
    player_bid_index = int(input("Your bid (Enter the index of the card in your hand): "))
    player_card = player_cards.pop(player_bid_index)
    
    computer_bid_card = get_computer_bid(diamond_card, computer_cards, player_card, len(diamond_cards), player_cards)
    computer_cards.remove(computer_bid_card)
    
    print("Your bid:", format_card(player_card))
    print("Computer's bid:", format_card(computer_bid_card))
    
    player_rank_value = get_rank_value(player_card[0])
    computer_rank_value = get_rank_value(computer_bid_card[0])
    
    if player_rank_value > computer_rank_value:
        return 'Player'
    elif player_rank_value < computer_rank_value:
        return 'Computer'
    else:
        return 'Tie'

def format_card(card):
    return f"{card[0]} of {card[1]}"

def print_cards(cards):
    for i, card in enumerate(cards):
        print(f"{i}: {format_card(card)}")

def update_scores(winner, diamond_card, scores):
    rank_value = get_rank_value(diamond_card[0])  
    if winner == 'Player':
        scores['Player'] += rank_value
    elif winner == 'Computer':
        scores['Computer'] += rank_value
    else:
        scores['Player'] += rank_value / 2
        scores['Computer'] += rank_value / 2
    return scores

def play_game():
    deck = initialize_deck()
    players = deal_cards(deck)
    computer_cards = players['Computer']
    diamond_cards = initialize_diamond_cards()  
    scores = {'Player': 0, 'Computer': 0}
    
    print("Let's play Diamonds!")
    for i in range(1, 14):
        print("\nRound", i)
        diamond_card = diamond_cards.pop(random.randint(0, len(diamond_cards) - 1))  # Randomly choose a diamond card
        winner = conduct_auction(diamond_card, players['Player'], computer_cards, diamond_cards)
        scores = update_scores(winner, diamond_card, scores)
        print("Scores:", scores)
    
    print("\nFinal Scores:")
    print("Player:", scores['Player'])
    print("Computer:", scores['Computer'])
    
    if scores['Player'] > scores['Computer']:
        print("Congratulations! You win!")
    elif scores['Player'] < scores['Computer']:
        print("Computer wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    deck = initialize_deck()
    diamond_cards = initialize_diamond_cards()  
    if len(diamond_cards) < 13:
        print("Insufficient diamond cards to play the game.")
    else:
        play_game()    
