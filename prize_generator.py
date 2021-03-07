import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for i in range(0, NUM_TRIALS):
    prize = ""
    round_wins = 0
    for x in range(0, 3):
        prize_num = random.randint(1, 100)
        prize += " "
        if 0< prize_num <= 1:
            prize += "gold"
            round_wins += 5

        elif 5 < prize_num <= 25:
            prize += 'silver'
            round_wins += 2

        elif 25 < prize_num <= 65:
            prize += 'copper'
            round_wins += 1

        else:
            prize += 'lead'

    winnings += round_wins

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings-cost))
else:
    print("Sorry, you lost ${}".format(cost-winnings))