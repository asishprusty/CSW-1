import string  # For punctuation removal

# Step 1: Read a sentence from the user
sentence = input("Enter a sentence: ")

# Step 2: Remove punctuation
cleaned = sentence.translate(str.maketrans('', '', string.punctuation))

# Step 3: Convert all words to lowercase and split into a list
words = cleaned.lower().split()

# Step 4: Count the frequency of each unique word
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Step 5: Sort the words alphabetically
sorted_words = sorted(word_counts.items())

# Step 6: Display formatted output
print("\n--- Word Frequencies ---")
for word, count in sorted_words:
    print(f"{word}: {count}", end=" ")
print()