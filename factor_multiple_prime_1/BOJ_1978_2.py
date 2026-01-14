# BOJ 1978_2

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
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    input = sys.stdin.readline
    _ = int(input().strip())
    nums = map(int, input().split())
    
    cnt = 0
    for x in nums:
        if is_prime(x):
            cnt += 1
    
    print(cnt)
    

if __name__ == "__main__":
    main()
