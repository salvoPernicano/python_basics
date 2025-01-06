import random

def print_play():
    print("""
  PPPP   L       AAAAA   Y   Y
  P   P  L      A     A   Y Y
  PPPP   L      AAAAAAA    Y
  P      L      A     A    Y
  P      LLLLL  A     A    Y
    """)


print_play()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

playerCards = []
computerCards = []

def startGame():
    for x in range(2):
        playerCards.append(random.choice(nums))
        computerCards.append(random.choice(nums))

    print(f"Your cards are {playerCards[0]} & {playerCards[1]}")
    print(f"Computer cards are {computerCards[0]} & {computerCards[1]}")

startGame()

def calculateScore(cards):
    totalScore = 0
    for card in cards:
        totalScore += card
    return totalScore


playerScore = calculateScore(playerCards)

wantAnotherCard = input("Do you want another card? y/n  ")

if wantAnotherCard == "y":
    giveCard = True
else:
    giveCard = False

while giveCard:

    playerCards.append(random.choice(nums))
    playerScore = calculateScore(playerCards)  
    
    print(f"Your cards are now: {playerCards} (Score: {playerScore})")
    

    if playerScore > 21:
        giveCard = False
        print("You lost!")
        print(f"Your final hand: {playerCards} with score {playerScore}")
        break  
    wantAnotherCard = input("Do you want another card? y/n ")
    if wantAnotherCard != "y":
        giveCard = False

print(f"Your final hand: {playerCards} with score {playerScore}")


computerScore = calculateScore(computerCards)


if playerScore > 21:
    print(f"You lost! Computer wins with hand {computerCards} and score {computerScore}")
elif playerScore > computerScore:
    print(f"You won! Your final hand: {playerCards} with score {playerScore} against computer's hand: {computerCards} with score {computerScore}")
else:
    print(f"You lost! Your final hand: {playerCards} with score {playerScore} against computer's hand: {computerCards} with score {computerScore}")
