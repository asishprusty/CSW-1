# Program to perform various operations on student scores

# Step 1: Store scores in a list
scores = [78, 85, 92, 67, 88, 76, 95, 89, 73, 60]

print("Original Scores:", scores)

# Step 2: Find and display the average score
average_score = sum(scores) / len(scores)
print(f"\nAverage Score: {average_score:.2f}")

# Step 3: Determine the minimum and maximum scores
min_score = min(scores)
max_score = max(scores)
print(f"Minimum Score: {min_score}")
print(f"Maximum Score: {max_score}")

# Step 4: Display all scores above the average
above_average = [score for score in scores if score > average_score]
print("\nScores above average:", above_average)

# Step 5: Sort the list in descending order of scores
scores.sort(reverse=True)
print("\nScores in descending order:", scores)

# Step 6: Replace the three lowest scores with zero (0)
# (since the list is now sorted in descending order, the lowest are at the end)
scores[-3:] = [0, 0, 0]
print("\nScores after replacing three lowest with zero:", scores)
