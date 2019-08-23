import sys
user_input = int(sys.argv[1])


def is_prime(num, prime_set):
    for prime in prime_set:
        if num % prime == 0:
            return False
    return True

if __name__ == "__main__":
    primes = set({2,3})
    for prime in primes:
        if user_input % prime == 0:
            break
        print("It's prime!")