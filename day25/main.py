import sys
from math import ceil, sqrt


def main():
    card_pub_key = int(sys.argv[1])
    door_pub_key = int(sys.argv[2])

    exponent = baby_step_giant_step(7, door_pub_key, 20201227)
    encryption_key = transform(exponent, card_pub_key)
    print('Answer 1: {}'.format(encryption_key))


def find_encryption_key(card_pub_key, door_pub_key):
    card_loop = find_loop(card_pub_key)
    return transform(card_loop, door_pub_key)


def transform(loop_size, subject_num=7):
    result = 1
    for i in range(loop_size):
        result *= subject_num
        result %= 20201227
    return result


def find_loop(public_key):
    result = 1
    loop_count = 0
    while True:
        loop_count += 1
        result *= 7
        result %= 20201227
        if result == public_key:
            break
    return loop_count


def baby_step_giant_step(subject, expected, modulus):
    N = ceil(sqrt(modulus - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(subject, i, modulus): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(subject, N * (modulus - 2), modulus)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (expected * pow(c, j, modulus)) % modulus
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


if __name__ == '__main__':
    main()
