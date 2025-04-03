# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# # for num in num_list:
# #     print(num)

# # for num in num_list:
# #     print(num, end=" ")

# # print()

# # print(*num_list)

# # for num in num_list:
# #     if num>45:
# #         print(str(num)+" is over 45")
# #     else:
# #         print(str(num)+" is under 45")


# # Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number

# # for index, num in enumerate(num_list):
# #     if num == 36:
# #         # print("Number found at position: ", index, "fuck")
# #         print(f"Number found at position: {index} (fuck)")
# #         break

# count = 0
# for num in num_list:
#     if(num == 36):
#         break;
#     count += 1
# print(f"Number found at position: {count}")

# for i in range(1, 4):
#     j = i * 2
#     print(f"i is {i} and j is {j}")



# 8.7 - Simulate Events and Calculate Probabilities
# Solutions to review exercises


# from random import randint


# # Exercise 1
# # Write a function that simulates the roll of a die.
# def roll():
#     """Return random integer between 1 and 6"""
#     return randint(1, 6)


# # Exercise 2
# # Simulate 10,000 rolls of a die and display the average number rolled.
# num_rolls = 10_000
# total = 0

# for trial in range(num_rolls):
#     total = total + roll()

# avg_roll = total / num_rolls

# print(f"The average result of {num_rolls} rolls is {avg_roll}")

# def get_second_element(item):
#     return item[1]

# items = [(4, 1), (1, 2), (-9, 0)]
# items.sort(key=get_second_element)
# print(items)

data = ((1, 2), (3, 4))

for i in data:
    print(f"Row {data.index(i)+1} sum: {sum(i)}")