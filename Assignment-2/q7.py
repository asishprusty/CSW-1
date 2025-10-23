# Program to demonstrate set comprehension, dictionary comprehension, and lambda sorting

# Step a: Accept a list of integers with duplicates
numbers = [4, 2, 7, 4, 2, 4, 9, 7, 9, 9]
print("Original List:", numbers)

# Step b: Remove duplicates using set comprehension
unique_numbers = {num for num in numbers}
print("\nUnique Numbers (using set comprehension):", unique_numbers)

# Step c: Construct a frequency dictionary using dictionary comprehension
freq_dict = {num: numbers.count(num) for num in unique_numbers}
print("\nFrequency Dictionary (using dict comprehension):", freq_dict)

# Step d: Sort numbers by descending frequency using lambda expression
sorted_by_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
sorted_numbers = [num for num, freq in sorted_by_freq]

print("\nNumbers sorted by descending frequency:", sorted_numbers)
