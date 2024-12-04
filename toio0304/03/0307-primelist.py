def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): #idk y dis can judge primes??? 
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

try:
    n = int(input("Type Any Integer Here: "))
    prime_list = primes_up_to(n)
    print(f"{n} follows those primes: {prime_list}")
except ValueError:
    print("ERROR: Type Valid Number(Integer)")
