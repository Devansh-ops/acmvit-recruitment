# acmvit-recruitment
Projects for the recruitment into Association of Computing Machinery, VIT Vellore

# Question for Cyber Security
Decrypt the given ciphertext encrypted using a monoalphabetic cipher:
ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz

Your response should contain the original plaintext message, the key/shift used for encryption/decryption & an explanation of the decryption process used by you. (Brute Force Attack will not be considered a valid response)

# Solution

plaintext : silencelaysteadilyagainstthewoodandstoneofhillhouseandwhateverwalkedtherewalkedalone

shift/key : 21

## How-to

Monoalphabetic ciphers are considered very weak because of some inherent flaws. The fact that two characters are always in pair, plus the inherent letter frequency in english language, both can be used to crack monoalphabetic code relatively easily.

## Types of 'monoalphabetic' cipher
- Caeser sipher or shift cipher
- Substitution cipher

## Try 1
For try one, let us suppose the cipher used is a caeser cipher, then, there are only 26 possibilities for the shift. What we can do is shift the alphabets by some key in range 0 to 25, and check if the substituted result makes sense.

For that, first, we create a list of alphabets, alp. Then we create a dictionary containing the alphabets as keys and values as their shifted value. Note that the alphabets are shifted in reverse for a key for decryption.

Then, we create a string with the alphabets substituted as per the caeser cipher and key.

We check if the string makes sense. If the key does make sense, you have the decrypted text. For checking, we can also see if the decrypted text contains the common english words like 'the' or 'is'.

## Try 2
Suppose the shift is random, we can use the fact that english language inherently uses some particular alphabets, two letter words, three letter words etc more than others of in a relative percentage 
wiki: https://en.wikipedia.org/wiki/Letter_frequency

We can then use that fact to decrypt monoalphabetic ciphers. As this time, we could get the result using Try 1, this possibility is not explored. If you want me to demonstrate, please let me know via my email devansh.sachinkumar2020@vitstudent.ac.in .
