import string

# List of lowercase alphabet letters
alphabet = list(string.ascii_lowercase)

# Get user inputs
direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
shift_number = int(input("Type the shift for encryption/decryption: \n"))
message = input('Type your message:\n').lower()

# Caesar Cipher function for both encoding and decoding
def ceasar(message_cde_decode, number, encode_decode):
    mot_final = ''
    # Reverse the shift if decoding
    if encode_decode == 'decode':
        number *= -1
    
    for char in message_cde_decode:
        if char in alphabet:  # Only process alphabetic characters
            shifted_index = (alphabet.index(char) + number) % len(alphabet)
            mot_final += alphabet[shifted_index]
        else:
            mot_final += char  # Keep non-alphabetic characters (e.g., space, punctuation)
    
    return mot_final

# Main logic to choose between encode and decode
if direction == 'encode':
    encrypted_message = ceasar(message, shift_number, 'encode')
    print(f"Here is the encoded message: {encrypted_message}")
elif direction == 'decode':
    decrypted_message = ceasar(message, shift_number, 'decode')
    print(f"Here is the decoded message: {decrypted_message}")
else:
    print("Invalid input! Please choose 'encode' or 'decode'.")
