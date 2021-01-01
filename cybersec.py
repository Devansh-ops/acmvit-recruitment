encrypted = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

alp = list('abcdefghijklmnopqrstuvwxyz') # list of alphabets

dict1 = {}
for key in range(26):
    for i in range(26):
        dict1[alp[i]] = alp[(i-key)%26] # shift backwards by key values. if the
                                        # number becomes negative, it counts back from 'z'
                                        # (cuz using % 26)
    decrypted = '' # empty string
    for char in encrypted: # add the shifted character for a character in encrypted text
        decrypted += dict1[char]
    #if 'the' in decrypted or 'and' in decrypted:     # can be used to check if the decrypted text has frequently used english words
        #print("Plain text for key",key,"is",decrypted)
    print("Plain text for key",key,"is",decrypted)

message = '''
For try one, let us suppose the cipher used is a caeser cipher, then, there are only 26 possibilities for the shift. What we can do is shift the alphabets by some key in range 0 to 25, and check if the substituted result makes sense.

For that, first, we create a list of alphabets, alp. Then we create a dictionary containing the alphabets as keys and values as their shifted value. Note that the alphabets are shifted in reverse for a key for decryption.

Then, we create a string with the alphabets substituted as per the shift.

We check if the string makes sense. If the key does make sense, you have the decrypted text. For checking, we can also see if the decrypted text contains the common english words like 'the' or 'is'.

from above,

plaintext : silencelaysteadilyagainstthewoodandstoneofhillhouseandwhateverwalkedtherewalkedalone
shift/key : 21
'''
print(message)
