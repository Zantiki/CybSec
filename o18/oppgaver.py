import math
import random
from functools import reduce
from sympy import mod_inverse


def oppgave_1():
    print("\nOPPGAVE 1 A")
    print(72, "(10)=(2)", int_to_binary(72))
    print(136, "(10)=(2)", int_to_binary(136))

    print("OPPGAVE 1 B")
    to_mod = binary_to_int(list("10001"))
    to_mod_bin = "10001"
    bin_72 = "1001000"
    bin_136 = "10001000"
    bin_base = "11"
    print("11^72%10001", "=", bin_modulo_exponent_solve(int_to_binary(11), 72, int_to_binary(10001)))
    print("11^136%10001", "=",bin_modulo_exponent_solve(int_to_binary(11), 136, int_to_binary(10001)))
    print("OPPGAVE 1 C")
    print("a,", gcd(1262, 10001))
    print("b,", gcd(1814, 10001))
    print("OPPGAVE 1 D")
    print("a*b%10001 =", (1814 * 1262) % 10001)


def oppgave_2():
    print("\nOPPGAVE 2")
    public, private = generate_keypair(137, 131)
    encrypted = encrypt(private, chr(42))
    print("public key:", public)
    print("private key:", private)
    print("encrypted:", encrypted)
    decrypted = decrypt(public, encrypted)
    print("decrypted:", ord(decrypted), "expected 42")

def oppgave_3():
    print("\nOPPGAVE 3")
    print("a) pollard 1829:", pollard(1829, 5)[0])
    print("OPPGAVE 3 B")

    # Finn potenser av a som resulterer i at gcd((a % n) - 1, n) > 1
    print("b) pollard 18779:", pollard(18779, 2)[1], "er laveste m som fungerer")
    print("b) pollard 42583:", pollard(42583, 2)[1], "er laveste m som fungerer")
    print("Generelle regelen for M er å finne potenser av a som resulterer i at gcd((a_i_mte % n) - 1, n) > 1 ")
    print("c) pollard 6319:", pollard(6319, 2)[0], "med m =", pollard(6319, 2)[1])


def oppgave_4():
    print("\nOPPGAVE 4")
    print("a) result is {} took {} iterations".format(pollard_rho(8051)[0], pollard_rho(8051)[1]))
    print("b) result is {} took {} iterations".format(pollard_rho(1517)[0], pollard_rho(1517)[1]))
    print("c) result is {} took {} iterations".format(pollard_rho(31861)[0], pollard_rho(31861)[1]))

def oppgave_5():
    print("\nOPPGAVE 5")
    explenation_a = "siden ((ek(x1) % n) * (ek(x2) % n)) % n == (ek(x1)ek(x2) % n )" \
                  ", \ninverse av utrykket blir da ((ek'(x1) % n) * (ek'(x2) % n)) % n == (x1x2 % n ) " \
                  "\nsom så kan krypteres som  ek(x1x2) % n igjen"
    explenation_b = "Dette er et eksempel på et klartekst-angrep hvor man kan bruke kunnskapen om " \
                    "\nklarteksten til et chiffer for å finne de andre. Dette gjøres ved å genere og teste nøkler som" \
                    "\nresulterer i at chifferet blir den kjente klarteksten. Man kan så anvende disse nøklene for å" \
                    "\nforsøke å dekryptere teksten. Dette er betrakerlig raskere en ren brute-force"
    print("a):", explenation_a)
    print("\nb):", explenation_b)

def oppgave_6():
    print("\nOPPGAVE 6")
    expelenation_a = "I RSA er p og q definert som primtall noe som impliserer at differansen" \
                     "\nalltid vil være et partall, som kan utrykkes ved 2d, hvor d er et heltall"
    expelenation_b = "d er et gitt heltall og d² vil alltid være et kvadrat av d.  n er definert som q*p," \
                     "\nvi kan da utrykke d = (q-p) / 2 og løse med kvadratsetning. d² = (q²-2qp+q²)/4 " \
                     "\n 2²Z = 4* (d² + n) kan da utrykkes som (q²+2qp+q²) som er lik (q+p)², vi får da utrykket" \
                     "\n 2²Z = (q+p)² der Z er et gitt kvadrat-tall "
    expelenation_c = "Vi kan bruke pollard_rho for å finne en faktor og med den så kan vi finne den andre "
    factor1 = pollard_rho(152416580095517)[0]
    factor2 = int(152416580095517 / factor1)

    print("a) ", expelenation_a)
    print("b) ", expelenation_b)
    print("c) ", expelenation_c)
    print("d) 152416580095517 består av faktorene:", factor1, "*", factor2)

def pollard_rho(n) -> tuple:
    x = 2
    y = x
    d = 1
    iterations = 0
    while d == 1:
        iterations += 1
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x - y), n)
    if d == n:
        return None, iterations
    else:
        return d, iterations


def f(x, n):
    return (x*x + 1) % n

def pollard(n, base):
    # defining base
    a = 2

    i = 1

    while(True):

        a = (a**i) % n
        d = gcd((a-1), n)
        if (d > 1):

            #return the factor
            return d, i

            break

        i += 1

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    print(key, n)
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in list(plaintext)]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    print(key, n)
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(int((char ** key) % n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    #d = multiplicative_inverse(e, phi)
    # d = mod_inverse(e, phi)
    _, d, _ = egcd(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
    print(e, "vs", temp_phi)
    if temp_phi == 1:
        return d + phi
    return d+phi


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bin_modulo_exponent_solve(base, exponent, moduluo):
    base = binary_to_int(list(base))
    exponent = list(int_to_binary(exponent))
    moduluo = binary_to_int(list(moduluo))
    power_of_2 = [2**x for i, x in enumerate(range(len(exponent)-1, 0, -1)) if exponent[i] == "1" ]

    modulos = []
    power_of_2.sort()
    for i in range(len(power_of_2)):
        y = 0
        if i != 0:
            y = i - 1

        steps = int(power_of_2[i] / power_of_2[y])
        mod_part = 1
        for step in range(steps):
            if steps == 1:
                modulos.append((base ** power_of_2[i]) % moduluo)
            else:
                mod_part = mod_part * modulos[y]
        if len(modulos) == i+1:
            continue
        modulos.append(mod_part)



    multiplied = reduce((lambda x, y: x * y), modulos)

    return multiplied % moduluo


def int_to_binary(int_value):
    l = []
    while int_value > 0:
        bit = int_value%2
        int_value = math.floor(int_value/2)
        l = [int(bit)]+l
    ans = ''.join(map(str, l))
    return ans

def binary_to_int(binary_list):
    return sum([math.pow(2, x) for x in range(0, len(binary_list)) if int(binary_list[len(binary_list) - (x+1)]) != 0])


if __name__ == "__main__":
    oppgave_1()
    oppgave_2()
    oppgave_3()
    oppgave_4()
    oppgave_5()
    oppgave_6()