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
