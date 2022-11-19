import caesar_art

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    encrypted_text = ""

    for letter in text:
        position = alphabet.index(letter) # returns position of letter in alphabet
        new_position = position + shift

        if new_position <= 25:
            encrypted_text += alphabet[new_position]

        elif new_position > 25:
            new_position = new_position % 26
            encrypted_text += alphabet[new_position]

    print(f"The encoded text is {encrypted_text}.")

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):

    decrypted_text = ""

    for letter in text:
        old_position = alphabet.index(letter) # returns position of letter in alphabet
        position = old_position - shift

        if position >= 1 and position <= 25:
            decrypted_text += alphabet[position]

        elif position < 1:
            position = position % 26 # convert back to index between 0 - 25
            decrypted_text += alphabet[position]

    print(f"The decoded text is {decrypted_text}.")

# Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):

    final_text = ""

    # If shift number is > 26
    shift = shift % 26

    for letter in text:

        # For number/symbol/space
        if letter not in alphabet:
            final_text += letter

        # For alphabets
        else:
            position = alphabet.index(letter) # returns position of letter in alphabet

            # Decrypt text
            if direction == "decode":
                position = position - shift

                if position >= 1 and position <= 25:
                    final_text += alphabet[position]

                elif position < 1:
                    position = position % 26 # convert back to index between 0 - 25
                    final_text += alphabet[position]

            # Encrypt text
            elif direction == "encode":
                new_position = position + shift

                if new_position <= 25:
                    final_text += alphabet[new_position]

                elif new_position > 25:
                    new_position = new_position % 26
                    final_text += alphabet[new_position]

    print(f"The {direction}d result is {final_text}")
        

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alternatively, we can also consider to add another set of alphabets to the alphabet list so that if the index exceeds 25, it can continue to account for the extended list

print(caesar_art.logo)

user_continue = "yes"

while user_continue == "yes": 
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))

    caesar(text=user_text, shift=user_shift, direction=cipher_direction)
    user_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.")

    if user_continue == "no":
        print("Goodbye!")


