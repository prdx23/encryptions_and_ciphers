

def monoalpha(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    for char in text:
        index = letters.index(char)
        new_text += letters[26 - index]
    return new_text


text = 'hello'
key = 4
cipher = monoalpha(text)
print('Cipher is ', cipher)
plaintext = monoalpha(cipher)
print('Plaintext is', plaintext)
