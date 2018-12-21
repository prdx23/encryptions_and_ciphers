

def ksa(key):
    # key scheduling algorithm
    s, j = list(range(256)), 0
    key = [int(x) for x in key]
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def prga(s):
    #  pseudo-random generation algo
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k


def encrypt(plaintext, key):
    s = ksa(key)
    prga_value = prga(s)
    cipher = [ord(char) ^ next(prga_value) for char in plaintext]
    return cipher


def decrypt(cipher, key):
    s = ksa(key)
    prga_value = prga(s)
    plaintext = [char ^ next(prga_value) for char in cipher]
    return ''.join(chr(char) for char in plaintext)


def main():
    text = 'hello'
    key = '1234'
    cipher = encrypt(text, key)
    print('Cipher is ', cipher)
    plaintext = decrypt(cipher, key)
    print('Plaintext is ', plaintext)


if __name__ == '__main__':
    main()
