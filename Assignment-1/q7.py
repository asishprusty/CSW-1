import string  # For punctuation removal

# Step 1: Read inputs
sentence = input("Enter a sentence: ")
separator = input("Enter a custom separator: ")

# Step 2: Remove punctuation
# Replace punctuation characters with empty string
cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

# Step 3: Split into words and convert to lowercase for consistent sorting
words = cleaned_sentence.split()
words = [word.lower() for word in words]  # Optional: make sorting case-insensitive

# Step 4: Sort words in reverse alphabetical order
words.sort(reverse=True)

# Step 5: Join words using the custom separator
result = separator.join(words)

# Step 6: Display the result
print("\n--- Sorted Words ---")
print(result)