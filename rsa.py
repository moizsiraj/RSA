import sympy as sp


def validInputs(p, q):
    return sp.isprime(p) and sp.isprime(q)


def checkCoprime(n):
    coprimes = []
    for i in range(0, n):
        if sp.gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes


def getKeys():
    values = []
    p = int(input('input p: '))
    q = int(input('input q: '))
    n = -1
    if not validInputs(p, q):
        print('invalid p or q or both')
    else:
        n = p * q
    z = (p - 1) * (q - 1)
    coprimes = checkCoprime(n)
    print('select e from given list')
    print(coprimes)
    e = int(input('e: '))
    d = int((1 + z) / e)
    values.append(e)
    values.append(d)
    values.append(n)
    print('PU: {' + str(e) + ', ' + str(n) + ' }')
    print('PR: {' + str(d) + ', ' + str(n) + ' }')
    return values


def encrypt(text, e, n):
    encrypted = []
    for i in text:
        value = -1
        if 65 <= ord(i) <= 90:
            value = ord(i) - 64
        elif 97 <= ord(i) <= 122:
            value = ord(i) - 96
        else:
            print('invalid character')
            exit(0)
        value = pow(value, e)
        value = value % n
        encrypted.append(value)
    print(encrypted)
    return encrypted


def decrypt(text, d, n):
    decrypted = []
    for character in text:
        temp = pow(character, d)
        temp = temp % n
        decrypted.append(chr(temp + 64))
    print(decrypted)
    return decrypted


def RSA():
    text = input('input text to be encrypted:')
    values = list(getKeys())
    e = int(values[0])
    d = int(values[1])
    n = int(values[2])
    encrypted = encrypt(text, e, n)
    decrypted = decrypt(encrypted, d, n)


RSA()
