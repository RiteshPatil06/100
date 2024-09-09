#caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("welcome to caesar cipher!")
word = input("Enter the word you wanna encrypt: ").lower()
shift = int(input("Enter the shift value: "))



def encrypt(og_word, og_shift):
    encrypted_word = ""


    for letter in og_word:
        shifted_position = alphabet.index(letter) + og_shift
        shifted_position %= len(alphabet)
        encrypted_word += alphabet[shifted_position]

    print(f"The encoded word is: {encrypted_word}")

encrypt(og_word = word, og_shift = shift)    

new_word = encrypt.encrypted_word
def decrypt(og_word, og_shift):
    decrypted_word = ""
    

    for letter in og_word:
        shifted_position = alphabet.index(letter) - og_shift
        decrypted_word += alphabet[shifted_position]

    print(f"The decoded word is: {decrypted_word}")

decrypt(og_word= new_word, og_shift= shift)        