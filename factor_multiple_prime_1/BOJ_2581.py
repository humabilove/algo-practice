# BOJ 2581

import sys
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True


def main():
    input = sys.stdin.readline
    M = int(input().strip())
    N = int(input().strip())
    primes = []
    for i in range(M, N+1):
        if is_prime(i):
            primes.append(i)
    
    if len(primes) == 0:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))
    

if __name__ == "__main__":
    main()
