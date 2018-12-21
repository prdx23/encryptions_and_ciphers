
def compute_public_value(p, g, secret):
    return g ** secret % p


def compute_symmetric_key(x, p, secret):
    return x ** secret % p


#  public keys p and g
p = 23
g = 9


secret_a = int(input('enter person A"s secret key:'))
secret_b = int(input('enter person B"s secret key:'))

public_a = compute_public_value(p, g, secret_a)
public_b = compute_public_value(p, g, secret_b)

print('person A shared public value: ,', public_a)
print('person B shared public value: ,', public_b)


key_a = compute_symmetric_key(public_b, p, secret_a)
key_b = compute_symmetric_key(public_a, p, secret_b)

print('person A generated private key:', key_a)
print('person B generated private key:', key_b)
