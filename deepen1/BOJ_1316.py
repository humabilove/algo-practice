# BOJ 1316

import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    count = 0
    while N:
        s = input().strip()
        is_group = True
        alpha = [s[0]]
        for i in range(1,len(s)):
            present = s[i]
            before = s[i-1]
            if present == before:
                # 현재의 것이 이전 것과 같으면
                continue
            else:
                # 현재의 것이 이전 것과 다를 때
                if present in alpha:
                    # 리스트 안에 이미 들어있다면 false
                    is_group = False
                    break
                else:
                    # 리스트 안에 들어있지 않다면 현재 것 리스트에 추가하기
                    alpha.append(present)

        if is_group:
            count += 1        
                    
        N -= 1
    print(count)
if __name__ == "__main__":
    main()
