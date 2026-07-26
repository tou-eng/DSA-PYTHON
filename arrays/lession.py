
# """
# This function takes a list of numbers as input and returns the sum of all the elements in the list.

# Parameters:
# numbers (list): A list of numerical values.

# Returns:
# int/float: The sum of all the elements in the list.
# # """
# # def sumL(numbers):
# #         total = 1
# #         for num in numbers:
# #             total *= num
# #         return total
# # arrays = [1, 2, 3, 4, 5]
# # result = sumL(arrays)
# # print(result)



# """
#     This function takes a list of numbers as input and returns the largest number in the list.

#     Parameters:
#     numbers (list): A list of numerical values.

#     Returns:
#     int/float: The largest number in the list.
# """


# # def largest_number(numbers):
# #     largest = numbers[0]

# #     for i in range(1, len(numbers)):
# #         if numbers[i] > largest:
# #             largest = numbers[i]

# #     return largest


# # arrays = [1, 2, 3, 4, 5]
# # result = largest_number(arrays)
# # print(result)

# # Define a function called match_words that takes a list of words 'words' as input
# def match_words(words):
#     # Initialize a counter 'ctr' to keep track of matching words
#     ctr = 0

#     # Iterate through each word in the input list 'words'
#     for word in words:
#         # Check if the word has a length greater than 1 and its first and last characters are the same
#         if len(word) > 1 and word[0] == word[-1]:
#             # If the condition is met, increment the counter 'ctr'
#             ctr += 1

#     # Return the final count of matching words
#     return ctr


# # Call the match_words function with the list ['abc', 'xyz', 'aba', '1221'] as input and print the result
# print(match_words(['abc', 'xyz', 'aba', '1221', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq']))

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)

