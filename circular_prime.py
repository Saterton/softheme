def circular_prime(number):
    primes = [True for i in range(0, number + 1)]
    for i in range(2, int(number ** (1 / 2))):
        if primes[i]:
            for j in range(i ** 2, number + 1, i):
                primes[j] = False
    result = []
    for i in range(0, number + 1):
        if primes[i]:
            length = len(str(i))
            for j in range(length):
                if not primes[int(str(i)[-j:] + str(i)[:-j])]:
                    break
            else:
                result.append(i)
    return len(result)


if __name__ == '__main__':
    print(circular_prime(1000000))
