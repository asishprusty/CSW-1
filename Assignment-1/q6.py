# Encryption and Decryption Program

# Function to encrypt a string
def encrypt(text):
    # Step 1: Reverse the string
    reversed_text = text[::-1]
    
    # Step 2: Swap every adjacent pair of characters
    chars = list(reversed_text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    encrypted_text = ''.join(chars)
    return encrypted_text


# Function to decrypt a string (reverse of encryption)
def decrypt(encrypted_text):
    # Step 1: Swap adjacent pairs back
    chars = list(encrypted_text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    swapped_back = ''.join(chars)
    
    # Step 2: Reverse the string again
    original_text = swapped_back[::-1]
    return original_text


# --- Main Program ---
user_input = input("Enter a string to encrypt: ")

# Encrypt and decrypt
encrypted = encrypt(user_input)
decrypted = decrypt(encrypted)

# Display results
print("\n--- Results ---")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")