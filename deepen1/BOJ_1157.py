# BOJ 1157

import sys

def main():
    input = sys.stdin.readline
    
    string = input().strip()
    string = string.upper()
    alpha = [0]*26
    for ch in string:
        idx = ord(ch) - 65
        alpha[idx] += 1
    
    max_index = 0
    is_one = True
    for i in range(1,26):
        M = alpha[max_index]
        if M < alpha[i]:
            max_index = i
            is_one = True
        elif M == alpha[i]:
            is_one = False
        
    if is_one:
        print(chr(max_index+65))
    else:
        print("?")

if __name__ == "__main__":
    main()
