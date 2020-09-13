from hashlib import sha1, pbkdf2_hmac
from itertools import product
import binascii
from pyspark import SparkContext
import os
import string


def test():
    possible = ["Q", "w", "E"]
    combos = product(possible, repeat=3)
    string_list = ["".join(x) for x in combos]
    print(string_list)
    for poss in string_list:
        encrypted = encrypt(poss, "Saltet til Ola")
        print(poss, encrypted, "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6")
        if crack_wrapper("ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6", poss, "Saltet til Ola"):
            print("Found password")
            break

def encrypt(string_to_hash, salt_to_hash):
    bytes_hash = pbkdf2_hmac('sha1', password=string_to_hash.encode(),
                              salt=salt_to_hash.encode(), iterations=2048)
    return bytes_hash.hex()

def gen_possible(limit):
    possible = list(string.printable)
    possible = possible[:62]
    possible += ["æ", "Æ", "ø", "Ø", "å", "Å", "_", "-", " "]
    # print(possible)
    combos = product(possible, repeat=limit)
    return combos

def crack_wrapper(expected_hash, password_to_try, salt):
    encrypted = encrypt(password_to_try, salt)
    # print(password_to_try, encrypted, expected_hash)
    if expected_hash == encrypted:
        return password_to_try
    else: return False


if __name__=="__main__":

    batch_size = 50000
    sc = SparkContext.getOrCreate()
    expected_hash = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6"
    expected_salt = "Saltet til Ola"
    print("Attempting crack on {} cores".format(os.cpu_count()))
    print("You can access spark-gui on http://localhost:4040/jobs/")
    total_processed = 0

    for i in range(1, 5):
        print("Processing strings of length: ", i)
        end_of_iter = False
        possible_pass = gen_possible(i)

        while True:
            string_list = []

            for i in range(batch_size):
                try:
                    string_list.append("".join(possible_pass.__next__()))
                except StopIteration:
                    end_of_iter=True
                    break
            total_processed += i

            # print(string_list)
            rdd = sc.parallelize(string_list, 4)
            # print(crack_wrapper(password_to_try=string_list[0], salt=expected_salt, expected_hash=expected_hash))
            res = rdd.map(lambda x: crack_wrapper(salt=expected_salt, expected_hash=expected_hash, password_to_try=x))
            res = res.collect()

            result = [x for x in res if isinstance(x, str)]
            if len(result) > 0:
                print("Result: ", result)
                input("result found, kill? (press enter)")
                break
            print("{} possibilities processed,  no password found".format(total_processed))
            if end_of_iter:
                break

