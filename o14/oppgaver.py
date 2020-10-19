import math
import numpy as np
from numpy.linalg import inv, det
import string
import random

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m
    return (m * congruence(m, -b, a) + b)


def oppgave1():
    ledd1 = 232 + (22 * 7)
    ledd2 = congruence(1, math.pow(18, 2), 8)
    print(ledd2)
    print(ledd1 - ledd2)

def oppgave2a():
    # https://demonstrations.wolfram.com/ModularArithmeticTables/
    N = 12
    arr = np.fromfunction(lambda i,j:(i+1)*(j+1) % N, (N-1,N-1))
    for row in arr:
        print(row)

def oppgave2b():
    answer = "1, 5, 7, 11"
    print(answer)

def oppgave2c():
    # https://scipython.com/blog/visulaizing-modular-multiplication-tables/
    answer = "Alle rader/kolonner som inneholder 1 er primtall, og da alle tall med 0 er delelige" \
             " vil 1 naturligvis ikke være del av disse"
    print(answer)

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def oppgave3b():
    N = 9
    z10 = np.fromfunction(lambda i,j:(i+1)*(j+1) % N, (N-1,N-1))
    # Finn den inverse matrisen a over z10
    a = np.array([
        [2, -1],
        [5, 8]
    ])
    print(z10)
    result = inv(a)
    print(det(a))
    multi_inverse = modInverse(det(a), N)
    result = result * 21 * multi_inverse # Matrise med omformet determinant
    result = a * result
    print(result)

def oppgave3a():
    N = 10
    z10 = np.fromfunction(lambda i,j:(i+1)*(j+1) % N, (N-1,N-1))
    # Finn den inverse matrisen a over z10
    a = np.array([
        [2, -1],
        [5, 8]
    ])
    print(z10)
    result = inv(a)
    print(det(a))
    multi_inverse = modInverse(det(a), N)
    result = result * 21 * multi_inverse # Matrise med omformet determinant
    result = a * result
    print(result)

def oppgave4a():
    print("29 Nøkler")

def oppgave4b():
    print("Vi kan kombinere med caesar-schiffer for å jobbe rundt frekvensanalysen. f.eks")

def oppgave4c():
    print("n! nøkler")


def encode_6(message, block_size, alphabet):
    chars = list(message)
    chars = [char.upper() for char in chars if char != " "]
    # Add padding
    while len(chars) % block_size != 0:
        chars.append(" ")

    blocks = [chars[x:x+block_size] for x in range(0, len(chars), block_size)]
    encrypted_blocks = []
    for block in blocks:
        key = random.randint(5, len(alphabet))
        encrypted_blocks.append((k_shift_encrypt(block, key, alphabet), key))

    print(encrypted_blocks)
    return encrypted_blocks




def oppgave6():
    alpha_nor = list(string.ascii_uppercase) + ['Æ', 'Ø', "Å", " "]
    message = "Dette er en test"
    key_value_pairs = encode_6(message, 5, alpha_nor)
    print("b = 5, N = 30, 3 Nøkler")
    print("Definition: x = x1x2x3... -> ek1(x1)ek2(x2)ek3(x3)...")
    print(key_value_pairs)
    decrypted = ""
    for code, key in key_value_pairs:
        num_code = []
        for letter in list(code):
            num_code.append(alpha_nor.index(letter))
        decrypted += k_shift_decrypt(num_code, key, alpha_nor)

    print(decrypted)



def k_shift_encrypt(message, k, alphabet):
    code = []
    for letter in message:
        code.append(alphabet.index(letter))

    result_string = ""
    new_code = []
    for num in list(code):
        new_num = (num + k) % len(alphabet)
        new_code.append(new_num)
    index = 0

    for num in new_code:
        result_string += alphabet[num]
        index += 1
    return result_string

def k_shift_decrypt(cipher_code, k, alphabet):
    result_string = ""
    new_code = []
    for num in list(cipher_code):
        new_num = (num - k) % len(alphabet)
        new_code.append(new_num)
    index = 0
    for num in new_code:
        result_string += alphabet[num]
        index += 1


    return result_string



def oppgave5():
    chiper = "YÆVFBVBVFRÅVBV"
    code = []
    alpha_nor = list(string.ascii_uppercase) + ['Æ', 'Ø', "Å"]
    for letter in list(chiper):
        code.append(alpha_nor.index(letter))

    for num in range(1, 20):
        print(k_shift_decrypt(code, num, alpha_nor))

    result = "HJERNEN ER ALENE"
    print(result)

if __name__ == "__main__":
    print("--- OPPGVAE 1 ---")
    oppgave1()
    print("--- OPPGAVE 2 ---")
    oppgave2a()
    oppgave2b()
    oppgave2c()
    print("--- OPPGAVE 3 ---")
    oppgave3a()
    oppgave3b()
    print("--- OPPGAVE 4 ---")
    oppgave4a()
    oppgave4b()
    oppgave4c()
    print("--- OPPGAVE 5 ---")
    oppgave5()
    print("--- OPPGAVE 6 ---")
    oppgave6()