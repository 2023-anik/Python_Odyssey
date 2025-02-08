#Figure out a way to store 9 & 9.0 as separate values in the set.

# a, b = str(9), str(9.0)
# st = (a, b)
# print(st)

st = {
    ("float", 9.0),
    ("int", 9)
}
print(st)