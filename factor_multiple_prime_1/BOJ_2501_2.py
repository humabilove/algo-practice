# BOJ 2501_2

import sys
import math

def kth_divisor(N: int, K: int) -> int:
    small = []
    large = []

    for i in range(1, int(math.isqrt(N)) + 1):
        if N % i == 0:
            small.append(i)
            j = N // i
            if j != i: # 제곱수면 중복 방지
                large.append(j)
    
    # small: 오름차순 (1, 2, 3, ...)
    # large: 내림차순으로 쌓임 (N, N/2, ...) -> 뒤집으면 오름차순
    divisors = small + large[::-1]
    
    return divisors[K-1] if K <= len(divisors) else 0

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    print(kth_divisor(N, K))
    

if __name__ == "__main__":
    main()
