def main():
  myMessage = input("Write your message: ")
  myKey = int(input("Write your key: "))

  ciphertext = encryptMessage(myKey, myMessage)
  print(ciphertext + '|')

def encryptMessage(a, b):
  ciphertext = [''] * a

  for column in range(a):
    currentIndex = column

    while currentIndex < len(b):
      ciphertext[column] += b[currentIndex]

      currentIndex += a

  return ''.join(ciphertext)