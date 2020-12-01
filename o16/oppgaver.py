
import math
import string
from bitstring import BitArray

ALPHA = string.ascii_uppercase + "ÆØÅ"
sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]
sbox = [int(x) for x in sbox]

def oppgave1_a():
    print("OPPGAVE 1 A")
    keys = ["1000", "0011", "1111"]
    for key in keys:
        period = 0
        bits = [int(bit) for bit in list(key)]
        current_key = bits.copy()
        current_key.append(get_bit_1(current_key))
        while True:
            if len(current_key) % 4 == 0:
                period += 1
                if current_key[-4:] == bits:
                    break
            current_key.append(get_bit_1(current_key[-4:]))

        print(key, "has period", period)

        """exponent = len(list(key)) - 1
        period = math.pow(2, exponent)
        print(key, "has period: ", period)"""


def get_bit_1(bits):
    return sum(bits) % 2

def get_bit_2(bits):
    return (bits[0] + bits[3]) % 2


def oppgave1_b():
    print("OPPGAVE 1 B")
    keys = ["1000", "0011", "1111"]
    for key in keys:
        period = 0
        bits = [int(bit) for bit in list(key)]
        current_key = bits.copy()
        current_key.append(get_bit_1(current_key))
        while True:
            if len(current_key) % 4 == 0:
                period += 1
                if current_key[-4:] == bits:
                    break
            current_key.append(get_bit_2(current_key[-4:]))
        print(key, "has period", period)


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
    print("HMAC of", x)
    print(hmac(x, key, ipad, opad))
    print("b")
    x2 = list("0111")
    expected = hmac(x2, key, ipad, opad)
    real = "00000100"
    print(expected, "v.", real)


def oppgave_4():

    print("\nOPPGAVE 4")
    x = list("1101111110100001")
    x2 = list("0010110000011111")
    init_vector = list("0000")
    blocks1 = []
    blocks2 = []
    i = 0
    while i < len(x):
        y = 0
        temp1 = []
        temp2 = []
        while y < 4:
            temp1.append(x[i])
            temp2.append(x2[i])
            y += 1
            i += 1
        blocks1.append(temp1)
        blocks2.append(temp2)
    encrypted_list = cbc_hmac(blocks1, init_vector)
    print("CBC MAC", blocks1)
    encrypted_list = cbc_hmac(blocks1, init_vector)
    print(encrypted_list)
    print("CBC MAC", blocks2)
    encrypted_list = cbc_hmac(blocks2, init_vector)
    print(encrypted_list)

def oppgave_5():
    print("\nOPPGAVE 5")
    hex_string = "24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95"
    hex_key = "67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7"
    encrypted_string = "26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D6 1E"
    plain_text_list = [alpha_to_int([int(x, 16) % len(list(ALPHA))], "from") for x in hex_string.split()]
    """message_int_list = [list(BitArray(hex=x).bin) for x in hex_string.split()]
    key_int_list = [list(BitArray(hex=x).bin) for x in hex_key.split()]"""

    """message_int_list = [int(x, 16) for x in hex_string.split()]
    key_int_list = [int(x, 16) for x in hex_key.split()]
    encrypted_list = [int(x, 16) for x in encrypted_string.split()]"""

    message_int_list = [int(x, 16) for x in hex_string.split()]
    key_int_list = [int(x, 16) for x in hex_key.split()]
    encrypted_list = [int(x, 16) for x in encrypted_string.split()]

    blocks1 = []
    blocks2 = []
    blocks3 = []
    i = 0
    while i < len(message_int_list):
        y = 0
        temp1 = []
        temp2 = []
        temp3 = []
        while y < len(message_int_list):
            temp1.append(message_int_list[i])
            temp2.append(key_int_list[i])
            temp3.append(encrypted_list[i])
            y += 1
            i += 1
        blocks1.append(temp1)
        blocks2.append(temp2)
        blocks3.append(temp3)


    """byte_message = bytes.fromhex("".join(hex_string.split()))
    byte_key = bytes.fromhex("".join(hex_string.split()))"""
    encrypted = bad_aes_encrypt(blocks1[0], blocks2[0])
    # print(encrypted)
    #encrypted_copy = encrypted.copy()
    # encrypted_copy = [x % len(ALPHA) for x in encrypted]
    # print(encrypted_copy)
    decrypted = bad_aes_decrypt(blocks3[0], blocks2[0])

    result1 = []
    result2 = []
    # print([x % len(ALPHA) for x in encrypted], [x % len(ALPHA) for x in decrypted])
    for pair in zip(encrypted, decrypted):
        result1.append(hex(pair[0]))
        result2.append(hex(pair[1]))
        """for e1, e2 in zip(pair[0], pair[1]):
            result1.append(hex(e1))
            result2.append(hex(e2))"""
    print("Encrypted,", hex_string)
    result1 = [alpha_to_int([int(hex_num, 16) % len(ALPHA)], "from") for hex_num in result1]
    #result1 = [chr(hex_num) for hex_num in result1]
    print("Encrypted,", result1)
    print("Decrypted,", hex_string)
    result2 = [alpha_to_int([(int(hex_num, 16)) % len(ALPHA)], "from") for hex_num in result2]
    print("actual_decrypted:", result2)
    # print("expected_decrypted:", plain_text_list)


def oppgave_6():
    print("\nOPPGAVE 6")
    original_key = "2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C"
    key_hex_list = [int(x, base=16) for x in original_key.split()]

    words = []
    i = 1
    word = []
    while len(key_hex_list) > i-1:
        byte = key_hex_list[i-1]
        word.append(byte)
        if i % 4 == 0:
            words.append(word)
            word = []
        i += 1

    i = 0
    words_old = [[hex(x) for x in word] for word in words]
    print("before expansion:", words_old)

    while i < 6:
        word_last = words[len(words)-1]
        expanded = expand(word_last)

        current_word = expanded
        for y in range(len(words)):
            current_word = element_xor(current_word, words[y])
            words[y] = current_word
        i += 1

    words = [[hex(x) for x in word] for word in words]
    print("after expansion:", words)


def element_xor(word1, word2):
    xor_word = []
    for x, y in zip(word1, word2):
        xor_word.append(x ^ y)
    return xor_word


def expand(word):
    new_word = rotate(word, 4)
    # sub_word = sub_bytes(new_word)
    # Rcon ?
    new_word = element_xor(new_word, [1, 0, 0, 0])
    return new_word

def bad_aes_encrypt(plain, key):
    print("ENCRYPTING", plain, "with key", key )
    new_state = add_round_key(plain, key)
    print("Round key,", [x  for x in new_state])
    new_state = sub_bytes(new_state)
    print("Sub bytes,", [x for x in new_state])
    new_state = shift_rows(new_state)
    print("Shift rows,", [x for x in new_state])
    return new_state


def bad_aes_decrypt(plain, key):
    print("\nDECRYPTING", plain, "with key", key)
    new_state = shift_rows(plain)
    print("Shift rows,", [x for x in new_state])
    new_state = sub_bytes(new_state)
    print("Sub bytes,", [x for x in new_state])
    new_state = add_round_key(new_state, key)
    print("Round key,", [x for x in new_state], "\n")
    return new_state


"""def add_round_key(state, key):
    Nb = len(state)
    new_state = [[None for j in range(16)] for i in range(Nb)]
    for i, word in enumerate(state):
        for j, byte in enumerate(word):
            new_state[i][j] = byte ^ key[i][j]

    return new_state"""

def add_round_key(state, roundKey):
    for i in range(len(state)):
        state[i] = state[i] ^ roundKey[i]
        pass
    return state

def sub_bytes(state):
    for i in range(len(state)):
        state[i] = sbox[state[i]]
    return state

def shift_rows(state):
    for i in range(4):
        state[i*4:i*4+4] = rotate(state[i*4:i*4+4],i)
    return state

def rotate(word, n):
    return word[n:]+word[0:n]

"""def shift_rows(state):
    Nb = len(state)
    n = [word[:] for word in state]

    for i in range(Nb):
        for j in range(16):
            n[i][j] = state[(i+j) % Nb][j]

    return n"""

"""def sub_bytes(state):
    return [[sbox[byte] for byte in word] for word in state]"""


def cbc_hmac(blocks, init_vector):
    encrypted_list = []
    for block in blocks:
        encrypted = xor_caesar(init_vector, block)
        encrypted_list.append(encrypted)
        init_vector = encrypted
    return encrypted_list


def xor_caesar(init_vector, block):
    new_binary = []
    for bit1, bit2 in zip(init_vector, block):
        bit1 = int(bit1)
        bit2 = int(bit2)
        xor_result = (bit1 and not bit2) or (not bit1 and bit2)
        new_binary.append(int(xor_result))
    return caesar(new_binary)

def caesar(x_list):

    x = binary_to_int(x_list)
    return int_to_binary((x + 3) % 16)


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
    ans = ''.join(map(str, l))
    while len(list(ans)) < 4:
        ans = "0" + ans
    return ans


def binary_to_int(binary_list):
    return sum([math.pow(2, x) for x in range(0, len(binary_list)) if int(binary_list[len(binary_list) - (x+1)]) != 0])


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
    oppgave_4()
    oppgave_5()
    oppgave_6()