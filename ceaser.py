
def ceaser(text, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    for char in text:
        if char not in letters:
            continue
        new_char = ord(char) + key
        if new_char > ord('z'):
            new_char = ord(char) - ord('z') + ord('a') - 1
        new_text += chr(new_char)
    return new_text


text = 'hello'
key = 4
cipher = ceaser(text, key)
print('Cipher is ', cipher)
plaintext = ceaser(cipher, -1 * key)
print('Plaintext is', plaintext)
