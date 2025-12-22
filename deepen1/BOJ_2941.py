# BOJ 2941

import sys

def main():
    input = sys.stdin.readline
    
    s = input().strip()
    count = 0
    
    i = 0
    while i < len(s):
        three = s[i:i+3]
        two = s[i:i+2]
        if i+2 < len(s) and three == "dz=":
            count += 1
            i += 3
        elif i+1 < len(s) and two in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    print(count)

if __name__ == "__main__":
    main()
