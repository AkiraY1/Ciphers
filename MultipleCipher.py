from tkinter import *

def encrypt():
    if cipherType.get() == "Inverse" and userMessage.get() != "":
        InverseCipher()
    elif cipherType.get() == "Caesar" and userMessage.get() != "" and userKey.get() != "":
        CaesarCipher()
    elif cipherType.get() == "Transposition" and userMessage.get() != "" and userKey.get() != "":
        TranspositionCipher()

def InverseCipher():
    message = userMessage.get()
    translated = ""

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    result.configure(text = "Encrypted Message: " + translated)

def CaesarCipher():
    message = userMessage.get()
    key = int(userKey.get())
    mode = "encrypt"

    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%&*()-+=[]:;<>,"

    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == "encrypt":
                translatedIndex = symbolIndex + key
            elif mode == "decrypt":
                translatedIndex = translatedIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    
    result.configure(text = "Encrypted Message: " + translated)

def TranspositionCipher():
    def main():
        myMessage = userMessage.get()
        myKey = int(userKey.get())

        ciphertext = encryptMessage(myKey, myMessage)
        return ciphertext + '|'

    def encryptMessage(a, b):
        ciphertext = [''] * a

        for column in range(a):
            currentIndex = column

            while currentIndex < len(b):
                ciphertext[column] += b[currentIndex]
                currentIndex += a

        return ''.join(ciphertext)
    
    result.configure(text = "Encrypted Message: " + main())

window = Tk()
window.title("Multiple Ciphers")
window.geometry("1300x500")

cipherLabel = Label(window, text="Type of cipher [Inverse, Caesar, Transposition]:")
cipherLabel.pack()
cipherType = Entry(window, text="Enter here")
cipherType.pack()

keyLabel = Label(window, text="Key [if necessary]:")
keyLabel.pack()
userKey = Entry(window, text="Enter key here")
userKey.pack()

cipherLabel = Label(window, text="Message:")
cipherLabel.pack()
userMessage = Entry(window, text="Enter message here")
userMessage.pack()

enterMessage = Button(window, text="Enter ", command = encrypt)
enterMessage.pack()

result = Message(window, width=1000, text="[Encrypted message will appear here]")
result.pack()

window.mainloop()

#Hello
