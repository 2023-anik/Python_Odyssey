def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# string[:position]: Gets all characters up to (but not including) the specified position.
# character: Adds the replacement character.
# string[position + 1:]: Gets all characters after the specified position.