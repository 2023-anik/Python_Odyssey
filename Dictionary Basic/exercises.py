# captains = {} #Creating an empty dictionary
captains = dict() #Creating an empty dictionary

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" in captains:
    print(f"Exist")
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

# del captains["Discovery"]
# print(captains)