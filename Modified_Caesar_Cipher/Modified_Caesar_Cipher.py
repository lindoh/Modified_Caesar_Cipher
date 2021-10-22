#----------------------Modified Caesar Cipher----------------------------

#Ask the user for text to encrypt
text = input('Please enter a line of text to encrypt: ')
#Ask the user for a character shift value between 1 - 25
valid = False

#Throw an exception if wrong data is provided and Check for validity of the shift value 
while not valid:    
    try:    
        shift = int(input('Please enter a shift integer value (1 - 25): '))
    except:
        print('ERROR!!..Please enter a valid interger shift value (1 - 25)\n ')
        continue
        
    if shift < 1 or shift > 25:
        shift = int(input('Please enter a shift integer value (1 - 25): '))
    else:
        valid = True

#cipher will store the encrypted text
cipher = ''

#Iterate through the text string
for char in text:
    if not char.isalpha():      #If it is not an alphabet it remains unchanged
        cipher += char
    else:
        code = ord(char) + shift    #Find an ASCII equivalent code for this character
        if char.isupper():      #If it is an upper case character and greater than Z
            if code > ord('Z'):
                offset = code - ord('Z')
                code = ord('A') + offset - 1            #Start from 'A' again
        elif char.islower():      #If it is a lower case character and greater than z
            if code > ord('z'):
                offset = code - ord('z')
                code = ord('a') + offset - 1
       
        #Concatenate the valid character to cipher
        cipher += chr(code)

#Print Encrypted text
print(cipher)





