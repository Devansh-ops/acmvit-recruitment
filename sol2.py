#python3
#breaking monoalphabetic substitution cipher
# caeser cipher, with help of frequency

encrypted = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

count_letters = {a:encrypted.count(a) for a in set(encrypted)}

max_alp = ''.join([k for k,v in count_letters.items() if v == max(count_letters.values())])
# max_alp = max(count_letters, key=lambda x: count_letters[x])

# in english the most used character is e
# so max_alp would most probably be e
# hence, shift all the characters (in reverse) of how much e needs to be shifted to reach max_alp

alp = 'abcdefghijklmnopqrstuvwxyz'
key = alp.index(max_alp)-alp.index('e')

decrypted = ''

for char in encrypted:
    decrypted += alp[(alp.index(char)-key)%26]

print(decrypted)
