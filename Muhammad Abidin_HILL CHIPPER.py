#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Muhammad Abidin
# V3922032

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_len = len(key)

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            plain_char_idx = ord(char.lower()) - ord('a')
            key_char = key[i % key_len].lower()
            key_char_idx = ord(key_char) - ord('a')
            encrypted_char_idx = (plain_char_idx + key_char_idx) % 26
            encrypted_char = chr(encrypted_char_idx + ord('a'))

            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_len = len(key)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            encrypted_char_idx = ord(char.lower()) - ord('a')
            key_char = key[i % key_len].lower()
            key_char_idx = ord(key_char) - ord('a')

            decrypted_char_idx = (encrypted_char_idx - key_char_idx) % 26
            decrypted_char = chr(decrypted_char_idx + ord('a'))

            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

plaintext = "Muhammad Abidin"
kunci = "Wonoasri"

ciphertext = vigenere_encrypt(plaintext, kunci)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = vigenere_decrypt(ciphertext, kunci)
print("Decrypted Text:", decrypted_text)
# In[ ]:






# In[ ]:




