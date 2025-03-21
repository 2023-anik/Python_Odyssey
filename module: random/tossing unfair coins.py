import random

def unfair_coin_flip(probability_of_tails):
    """Randomly return 'heads' or 'tails'."""
    
    # if random.random() < probability_of_tails:
    #     return 'tails'
    # else:
    #     return 'heads'
    return "tails" if random.random() < probability_of_tails else "heads"

heads_tally = 0
tails_tally = 0

for i in range(10_000):
    if unfair_coin_flip(0.7) == 'heads':
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"Heads Tally: {heads_tally}\nTails Tally: {tails_tally}\nRatio: {ratio : .2f}")