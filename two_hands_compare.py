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
        
        print("Hand 1:", hand1_name, converted_cards1)
        print(" -  -  -  -  -  -  -  -  -  - ")
        print("Hand 2:", hand2_name, converted_cards2)
        
        result = compare_hands(hand1_name, hand2_name)
        print(result)