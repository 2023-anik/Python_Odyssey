import random

def flip_coin():
    """Randomly return 'heads' or 'tails'."""
    
    # print(random.choice(['heads', 'tails', 'edge', 'side', 'rim', 'none']))

    # if random.randint(0, 1) == 0:
    #     return 'heads'
    # else:
    #     return 'tails'
    # return 'heads' if random.randint(0, 1) == 0 else 'tails'
    return random.choice(['heads', 'tails'])
    
heads_tally = 0
tails_tally = 0

for i in range(10_000):
    if flip_coin() == 'heads':
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"Heads Tally: {heads_tally}\nTails Tally: {tails_tally}\nRatio: {ratio : .2f}")