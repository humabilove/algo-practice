# BOJ 9506

import sys

def main():
    input = sys.stdin.readline
    
    while True:
        n = int(input().strip())
        factors = []
        if n == -1:
            break
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        factors.pop()
        if n == sum(factors):
            print(f"{n} = ", end="")
            print(*factors, sep=" + ")
        else:
            print(f"{n} is NOT perfect.")

if __name__ == "__main__":
    main()
