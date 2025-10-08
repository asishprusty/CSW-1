# Paragraph Processing Program

def process_paragraph(paragraph):
    # Step 1: Remove extra spaces between words
    cleaned = ' '.join(paragraph.split())

    # Step 2: Convert to title case
    title_cased = cleaned.title()

    # Step 3: Count occurrences of vowels (A, E, I, O, U)
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_counts = {v: title_cased.upper().count(v) for v in vowels}

    # Step 4: Display character codes and counts
    print("\n--- Processed Text ---")
    print(title_cased)

    print("\n--- Vowel Counts ---")
    for v in vowels:
        print(f"{v} (ASCII {ord(v)}): {vowel_counts[v]}")


# --- Main Program ---
paragraph = input("Enter a paragraph: ")
process_paragraph(paragraph)