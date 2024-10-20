numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i < 2:
        continue
    else:
        f = i ** (1 / 2) #
        for a in range(2, int(f + 1)):
            if i % a == 0:
                is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ',  primes)
print("Not Primes: ", not_primes)