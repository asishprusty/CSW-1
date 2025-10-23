# Function to process dictionary based on data type of values
def process_data(data):
    # Helper function to check for prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = {}

    for key, value in data.items():
        # If value is a list → sum of prime numbers
        if isinstance(value, list):
            prime_sum = sum(num for num in value if is_prime(num))
            result[key] = prime_sum

        # If value is a tuple → product of odd numbers
        elif isinstance(value, tuple):
            product = 1
            has_odd = False
            for num in value:
                if num % 2 != 0:
                    product *= num
                    has_odd = True
            result[key] = product if has_odd else 0  # if no odd numbers, store 0

    return result


# ---- MAIN PROGRAM ----
data = {
    "A": [2, 3, 4, 5, 10],
    "B": (1, 2, 3, 4, 5),
    "C": [7, 8, 9],
    "D": (6, 7, 8)
}

# Process the dictionary
result = process_data(data)

# Display the result
print("Original Data:", data)
print("Processed Data:", result)
