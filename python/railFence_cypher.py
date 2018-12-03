"""
This program scrambles the words and make a simple cipher
"""

def scramble2Text(plainText):

    evenChars = ''
    oddChars = ''
    
    charCount = 0
    
    for ch in plainText:

        charCount += 1

        if charCount % 2 is 0:
            evenChars += ch
        else:
            oddChars += ch
        
    cipherText = oddChars + evenChars

    return cipherText

"""
This program unscrambles the above cipher
"""

def decryptMessage(cipherText):

    if len(cipherText) % 2 == 1:
        cipherText += ' '

    charCount = 0

    count = True

    evenChar = ''
    oddChar = ''

    for ch in cipherText:

        charCount += 1

        if charCount < (len(cipherText)+1) /2:
            oddChar += ch
        else:
            evenChar += ch


    plainText = ''

    x = int(charCount/2)

    for i in range(x):
        plainText = plainText + oddChar[i]
        plainText = plainText + evenChar[i]
            
    return plainText

"""
How I want the user to interact with the program
"""

def interface():

    want = True
    
    while (want == True):

        need = int(input("Would you like to encrypt[1] or decrypt[2]? "))

        if need == 1 :
            statement = input("Enter what you want to encrypt: ")
            print(scramble2Text(statement))
            want == True

        if need == 2 :
            statement = input("Enter what you want to decrypt: ")
            print(decryptMessage(statement))
            want == True

            
"""
Actual code for program. It runs in a loop so one can either decrypt
and encrypt, so conversations are easier to handle.
"""

interface()

input()
