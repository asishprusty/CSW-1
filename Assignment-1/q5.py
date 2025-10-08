decimal_num= int(input("Enter a decimal number: "))

binary_str = bin(decimal_num)[2:]       # Remove '0b' prefix
octal_str = oct(decimal_num)[2:]        # Remove '0o' prefix
hex_str = hex(decimal_num)[2:]          # Remove '0x' prefix

print("\n--- Base Conversions ---")
print(f"Binary: {binary_str}")
print(f"Octal: {octal_str}")
print(f"Hexadecimal: {hex_str.upper()}")


print("\n--- Digit Counts ---")
print(f"Binary digits: {len(binary_str)}")
print(f"Octal digits: {len(octal_str)}")
print(f"Hexadecimal digits: {len(hex_str)}")


reversed_binary = int(binary_str, 2)
reversed_octal = int(octal_str, 8)
reversed_hex = int(hex_str, 16)

print("\n--- Reverse Conversion (Verification) ---")
print(f"From Binary back to Decimal: {reversed_binary}")
print(f"From Octal back to Decimal: {reversed_octal}")
print(f"From Hexadecimal back to Decimal: {reversed_hex}")