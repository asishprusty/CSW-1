import math

def classify_numbers(numbers):
    """
    Classify integers into categories: Prime, Composite, Perfect Squares, and Perfect Cubes.
    Returns a dictionary with category names as keys and lists of numbers as values.
    """

    # Helper function to check for prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Helper function to check for perfect squares
    def is_perfect_square(n):
        if n < 0:
            return False
        return int(math.sqrt(n)) ** 2 == n

    # Helper function to check for perfect cubes
    def is_perfect_cube(n):
        if n < 0:
            return False
        cube_root = round(n ** (1 / 3))
        return cube_root ** 3 == n

    # Initialize classification dictionary
    classification = {
        "Prime": [],
        "Composite": [],
        "Perfect Squares": [],
        "Perfect Cubes": []
    }

    # Classify each number in the input list
    for num in numbers:
        if is_prime(num):
            classification["Prime"].append(num)
        elif num > 1:
            classification["Composite"].append(num)

        if is_perfect_square(num):
            classification["Perfect Squares"].append(num)
        if is_perfect_cube(num):
            classification["Perfect Cubes"].append(num)

    return classification


# ---- MAIN PROGRAM ----
# Example: user input
user_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Get classification
result = classify_numbers(numbers)

# Display results clearly
print("\nClassification Result:")
for category, values in result.items():
    print(f"{category}: {values}")
