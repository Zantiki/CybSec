
import math
import string

ALPHA = string.ascii_uppercase + "ÆØÅ"

def oppgave1_a():
    print("OPPGAVE 1 A")
    keys = ["1000", "0011", "1111"]
    for key in keys:
        exponent = len(list(key)) - 1
        period = math.pow(4, exponent)
        print(key, "has period: ", period)

def oppgave1_b():
    print("\nOPPGAVE 1 B")
    keys = ["1000", "0011", "1111"]
    for key in keys:
        exponent = len(list(key)) - 1
        period = math.pow(2, exponent)
        print(key, "has period: ", period)

def oppgave_2():
    print("\nOPPGAVE 2")

    key = 17
    cipher = autokey_encrypt_message("goddag", alpha_to_int([key], "from")[0])
    print("encryption:")
    print("goddag :", cipher)

    encrypted = [23, 8, 23, 12, 21, 2, 4, 3, 17, 13, 19]
    converted = "".join(alpha_to_int(encrypted, "from"))
    decrypted = autokey_cipher_message(converted, alpha_to_int([5], "from")[0], 'decrypt')
    print("decryption:")
    print(encrypted, ":", decrypted)

def oppgave_3():
    print("\nOPPGAVE 3")
    key = list("1001")
    ipad = list("0011")
    opad = list("0101")
    x = list("0110")
    print("a")
    print("HMAC of x:", x)
    print(hmac(x, key, ipad, opad))
    print("b")
    x2 = list("0111")
    expected = hmac(x2, key, ipad, opad)
    real = "00000100"
    print(expected, "v.", real)


def bit_mac(x, k, ip, op):
    x = bool(int(x))
    k = bool(int(k))
    ip = bool(int(ip))
    op = bool(int(op))

    operand_1 = (k and not op) or (not k and op)
    operand_2 = (k and not ip) or (not k and ip)
    mac_x = operand_1 or operand_2 or x

    return int(mac_x)


def hmac(x, k, ip, op):

    result_bits = []
    for x_char, k_char, ip_char, op_char in zip(x, k, ip, op):
        result_bits.append(bit_mac(x_char, k_char, ip_char, op_char))
    return int_to_binary(h(binary_to_int(result_bits)))


def int_to_binary(int_value):
    l = []
    while int_value > 0:
        bit = int_value%2
        int_value = math.floor(int_value/2)
        l = [int(bit)]+l
    return ''.join(map(str, l))


def binary_to_int(binary_list):
    return sum([math.pow(2, x) for x in range(0, len(binary_list)) if binary_list[len(binary_list) - (x+1)] != 0])


def h(x):
    return math.pow(x, 2) % math.pow(2, 8)

def alpha_to_int(chiper_list, mode):
    result = []
    alphabet_list = list(ALPHA)
    if mode == "to":
        for cipher in chiper_list:
            result.append(alphabet_list.index(cipher))
    if mode == "from":
        for cipher in chiper_list:
            result.append(alphabet_list[cipher])

    return result


def autokey_encrypt_message (messages, keys):
    return autokey_cipher_message(messages, keys, 'encrypt')


def autokey_cipher_message (messages, keys, mode):
    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        if mode == 'encrypt':
            text += ALPHA.find(key[k_index])
            key += i.upper()

        elif mode == 'decrypt':
            text -= ALPHA.find(key[k_index])
            key += ALPHA[text]
        text %= len(ALPHA)
        k_index += 1
        cipher.append(ALPHA[text])
    return ''.join(cipher)


if __name__ == "__main__":
    oppgave1_a()
    oppgave1_b()
    oppgave_2()
    oppgave_3()