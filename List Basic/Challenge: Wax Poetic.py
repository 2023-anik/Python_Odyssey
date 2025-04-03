import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]


list_nouns = random.sample(nouns, 3)
list_verbs = random.sample(verbs, 3)
list_adjectives = random.sample(adjectives, 3)
list_prepositions = random.sample(prepositions, 2)
list_adverbs = random.sample(adverbs, 1)


article1 = "An" if list_adjectives[0][0] in "aeiou" else "A"
article2 = "An" if list_adjectives[2][0] in "aeiou" else "A"


print(
    f"{article1} {list_adjectives[0]} {list_nouns[0]}\n\n"
    f"{article1} {list_adjectives[0]} {list_nouns[0]} {list_verbs[0]} {list_prepositions[0]} the {list_adjectives[1]} {list_nouns[1]}\n"
    f"{list_adverbs[0]}, the {list_nouns[0]} {list_verbs[1]}\n"
    f"the {list_nouns[1]} {list_verbs[2]} {list_prepositions[1]} {article2.lower()} {list_adjectives[2]} {list_nouns[2]}"
    )


# def make_poem():
#     """Create a randomly generated poem, returned as a multi-line string."""
#     # Pull three nouns randomly
#     n1 = random.choice(nouns)
#     n2 = random.choice(nouns)
#     n3 = random.choice(nouns)
#     # Make sure that all the nouns are different
#     while n1 == n2:
#         n2 = random.choice(nouns)
#     while n1 == n3 or n2 == n3:
#         n3 = random.choice(nouns)

#     # Pull three different verbs
#     v1 = random.choice(verbs)
#     v2 = random.choice(verbs)
#     v3 = random.choice(verbs)
#     while v1 == v2:
#         v2 = random.choice(verbs)
#     while v1 == v3 or v2 == v3:
#         v3 = random.choice(verbs)

#     # Pull three different adjectives
#     adj1 = random.choice(adjectives)
#     adj2 = random.choice(adjectives)
#     adj3 = random.choice(adjectives)
#     while adj1 == adj2:
#         adj2 = random.choice(adjectives)
#     while adj1 == adj3 or adj2 == adj3:
#         adj3 = random.choice(adjectives)

#     # Pull two different prepositions
#     prep1 = random.choice(prepositions)
#     prep2 = random.choice(prepositions)
#     while prep1 == prep2:
#         prep2 = random.choice(prepositions)

#     # Pull one adverb
#     adv1 = random.choice(adverbs)

#     if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
#         article = "An"
#     else:
#         article = "A"

#     # Create the poem
#     poem = (
#         f"{article} {adj1} {n1}\n\n"
#         f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}\n"
#         f"{adv1}, the {n1} {v2}\n"
#         f"the {n2} {v3} {prep2} a {adj3} {n3}"
#     )

#     return poem


# poem = make_poem()
# print(poem)