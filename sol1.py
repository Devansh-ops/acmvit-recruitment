encrypted = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

alp = list('abcdefghijklmnopqrstuvwxyz')

dict1 = {}
for key in range(26):
    for i in range(26):
        dict1[alp[i]] = alp[(i-key)%26]
    #decrypted = []
    decrypted = ''
    for char in encrypted:
    #    decrypted.append(dict1[char])
        decrypted += dict1[char]
    #decrypted = ''.join(decrypted)
    #if 'the' in decrypted or 'and' in decrypted:
        #print("Plain text for key",key,"is",decrypted)
    print("Plain text for key",key,"is",decrypted)
    
