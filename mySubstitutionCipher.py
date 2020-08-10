import sys, random

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

mode = input("encrypt or decrypt: ")

if mode == 'encrypt':
    random.shuffle(key)
    print("Your key is: " + ''.join(key))

    message = input("Message: ").lower()
    encryptedMessage = '`'

    for character in message:
        index  = ALPHABET.index(character)
        encryptedMessage += key[index]

    print("Encrypted Message: " + encryptedMessage)

if mode == 'decrypt':
    key = list(input("Input your key: "))
    message = input("Message: ").lower()
    decryptedMessage = ''

    for character in message:
        index = key.index(character)
        decryptedMessage += ALPHABET[index]
    
    print("Decrypted Message: " + decryptedMessage)
    

