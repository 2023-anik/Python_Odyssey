def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Here, split_and_join() is a function that takes a string as input and returns a string where each word is separated by a hyphen (-).