import art,random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,d_score):
    if u_score==d_score:
        print("Draw 🙃")
    elif u_score==0:
        print("HURRAY! YOU HIT A BLACKJACK 😎")
    elif d_score==0:
        print("YOU LOSE! OPPONENT HIT A BLACKJACK 😱")
    elif u_score>21:
        print("YOU WENT OVER AND LOSE! 😭")
    elif d_score>21:
        print("DEALER WENT OVER. YOU WIN! 😃")
    elif u_score>d_score:
        print("YOU WIN! 😃")
    else:
        print("YOU LOSE! 😤")




def blackjack():
    print(art.logo)
    user_cards=[]
    dealer_cards=[]
    user_score =-1
    dealer_score =-1

    is_gameover=False

    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_gameover:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}   Current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}, second card hidden ❓")

        if user_score==0 or dealer_score==0 or user_score>=21:
            is_gameover=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_gameover=True

    while dealer_score!=0 and dealer_score<17:
        dealer_cards.append(deal_card())
        dealer_score=calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    compare(user_score,dealer_score)
while input("Do you want to play the Blackjack game? Type 'y' for yes or 'n' for no:")=='y':
    print("\n"*100)
    blackjack()
