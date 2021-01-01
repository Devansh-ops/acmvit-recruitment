encrypted = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

alp = list('abcdefghijklmnopqrstuvwxyz')

dict1 = {}
for key in range(26):
    for i in range(26):
        dict1[alp[i]] = alp[(i-key)%26]
    decrypted = ''
    for char in encrypted:
        decrypted += dict1[char]
    #if 'the' in decrypted or 'and' in decrypted:
        #print("Plain text for key",key,"is",decrypted)
    print("Plain text for key",key,"is",decrypted)
