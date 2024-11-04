numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
num_ = 0
for num_ in numbers:
    if num_ == 1:
        continue
    is_prime = True
    for i in range(2, num_):
        if num_ % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num_)
    else:
        not_primes.append(num_)
print("Primes:", primes)
print("Not Primes:", not_primes)