from random import random

num_times_A_wins = 0
num_times_B_wins = 0

for i in range(10_000):

    votes_A = 0
    votes_B = 0

    if random() < 0.87:
        votes_A += 1
    else:
        votes_B += 1

    if random() < 0.65:
        votes_A += 1
    else:
        votes_B += 1

    if random() < 0.17:
        votes_A += 1
    else:    
        votes_B += 1

    if votes_A > votes_B:
        num_times_A_wins += 1
    else:
        num_times_B_wins += 1

print(f"Probability A wins: {num_times_A_wins / 10_000}")
print(f"Probability B wins: {num_times_B_wins / 10_000}")

    