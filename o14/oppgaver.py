import math
import numpy as np
from numpy.linalg import inv, det
import string

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

def oppgave3a():
    N = 10
    z10 = np.fromfunction(lambda i,j:(i+1)*(j+1) % N, (N-1,N-1))
    a = np.array([
        [2, -1],
        [5, 8]
    ])
    print(z10)
    result = det(a)
    print("det(a) = 3*7, og 7 en en multiplikativ invers")
    print(result)
    print(21*inv(a))

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
    print("--- OPPGAVE 5 ---")
    oppgave5()