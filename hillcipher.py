def matmult(a, b):
    zip_b = list(zip(*b))
    return [[sum(x * y for x, y in zip(row_a, col_b)) for col_b in zip_b]
            for row_a in a]


def encrypt(text, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    new_key = []
    for row in key:
        new_key.append([letters.index(char) for char in row])

    text = [[letters.index(char)] for char in text]
    cipher = [letters[x[0] % 26] for x in matmult(new_key, text)]
    return ''.join(cipher)


key = [
    ['g', 'y', 'b'],
    ['n', 'q', 'k'],
    ['t', 'a', 'o'],
    ['b', 'f', 'p'],
    ['u', 'r', 'p']
]
text = 'hello'
cipher = encrypt(text, key)
print('Cipher is ', cipher)
