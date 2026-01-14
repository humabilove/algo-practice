# BOJ 1978

import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(N):
        num = nums[i]
        isPrime = True
        if num == 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            count += 1
    print(count)
    

if __name__ == "__main__":
    main()
