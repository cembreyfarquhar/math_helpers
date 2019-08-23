import sys
user_input = int(sys.argv[1])


def is_prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                print(num, " is not prime")
                break
        else:
            print(num, " is prime!!!")
    else:
        print(num, " is not prime.")

if __name__ == "__main__":
    is_prime(user_input)