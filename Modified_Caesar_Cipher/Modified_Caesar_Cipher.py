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
            



