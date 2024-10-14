import string

# List of lowercase alphabet letters
alphabet = list(string.ascii_lowercase)

# Get user inputs
direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
shift_number = int(input("Type the shift for encryption/decryption: \n"))
message = input('Type your message:\n').lower()

# Encrypt function
def encrypt(message_original, number):
    final_pwd = ''
    for msg in message_original:
        if msg in alphabet:  # Encrypt only alphabetic characters
            cipher_msg = (alphabet.index(msg) + number) % len(alphabet)
            final_pwd += alphabet[cipher_msg]
        else:
            final_pwd += msg  # Keep non-alphabetic characters (e.g., space, punctuation)
    
    return final_pwd

# Decrypt function
def decrypt(password, key):
    mot_original = ''
    for pwd in password:
        if pwd in alphabet:
            decode = (alphabet.index(pwd) - key) % len(alphabet)
            mot_original += alphabet[decode]
        else:
            mot_original += pwd  # Keep non-alphabetic characters
    
    return mot_original

# Main logic to choose between encode and decode
if direction == 'encode':
    encrypted_message = encrypt(message, shift_number)
    print(f"Here is the encoded message: {encrypted_message}")
elif direction == 'decode':
    decrypted_message = decrypt(message, shift_number)
    print(f"Here is the decoded message: {decrypted_message}")
else:
    print("Invalid input! Please choose 'encode' or 'decode'.")
