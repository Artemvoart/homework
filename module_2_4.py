numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i < 2:
        continue
    p = True
    for num in range(2, int(i**0.5) + 1):
        if i % num == 0:
            p = False
            break
    if p == True:
        primes.append(i)
    else:
        not_primes.append(i)
print("Primes:", primes)
print("Not Primes:", not_primes)
