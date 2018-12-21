
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def modinv(e, n):
    #  returns the modular inverse (d) using e * d mod n = 1
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

    g, x, _ = egcd(e, n)
    return x % n


def generate_key_pair(p, q):
    #  find modulus
    n = p * q

    #  public key = (n, e), where e is not a factor of n(their gcd is 1)
    #  and 1 < e < phi, phi = (p-1)(q-1)
    e, phi = 2, (p - 1) * (q - 1)
    while e < phi and gcd(e, phi) != 1:
        e += 1

    public_key = (n, e)
    private_key = (n, modinv(e, phi))
    return public_key, private_key


def encrypt(msg, public_key):
    #  note: msg has to be numerical, or string converted to numerical
    #  cipher = (msg ^ e) mod n
    n, e = public_key
    cipher = (msg ** e) % n
    return cipher


def decrypt(cipher, private_key):
    #  plaintext = (cipher ^ d) mod n
    n, d = private_key

    if cipher > n:
        print('Choose larger prime numbers p and q')
        return 0

    plaintext = (cipher ** d) % n
    return plaintext


def main():
    #  first prime number (p)
    p = 521

    #  second prime number (q)
    q = 523

    msg = int(input('Enter msg (numerical):'))
    public_key, private_key = generate_key_pair(p, q)
    cipher = encrypt(msg, public_key)
    print(f'Encrypted msg: {cipher}')
    plaintext = decrypt(cipher, private_key)
    print(f'Decrypted msg: {plaintext}')


if __name__ == '__main__':
    main()
