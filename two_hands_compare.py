from pokerhand import PokerHand
import requests

hand_ranking = {
    "Royal Flush": 1,
    "Straight Flush": 2,
    "Four of a Kind": 3,
    "Full House": 4,
    "Flush": 5,
    "Straight": 6,
    "Three of a Kind": 7,
    "Two Pair": 8,
    "One Pair": 9,
    "High Card": 10
}

def convert_card(card):
    value = card['value']
    suit = card['suit'][0].upper()  # Take the first letter of the suit and convert it to uppercase
    if value == 'ACE':
        value = 'A'
    elif value == 'JACK':
        value = 'J'
    elif value == 'QUEEN':
        value = 'Q'
    elif value == 'KING':
        value = 'K'
    elif value == '10':
        value = 'T'
    return (value, suit)


def compare_hands(hand1, hand2):
    rank1 = hand_ranking[hand1]
    rank2 = hand_ranking[hand2]
    if rank1 < rank2:
        return "Hand 1 wins"
    elif rank1 > rank2:
        return "Hand 2 wins"
    else:
        return "It's a tie"
    
def poker_request2():
    deck_id = "new"
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=10"
    response = requests.get(url)
    if response.status_code == 200:
        cards = response.json()['cards']
        
        # Splitting list of cards using slicing
        deal_one = cards[:5]
        deal_two = cards[5:]
        
        # Converting into format for using with PokerHand app
        converted_cards1 = [convert_card(card) for card in deal_one]
        converted_cards2 = [convert_card(card) for card in deal_two]
        
        # Applying PokerHand function to the hands
        hand1 = PokerHand(converted_cards1)
        hand2 = PokerHand(converted_cards2)
        
        # Classifying both hands
        hand1_name = hand1.classify()
        hand2_name = hand2.classify() 
        result = compare_hands(hand1_name, hand2_name)
        return hand1_name, hand2_name, result, deal_one, deal_two
    else:
        return None, None, None, None, None
        