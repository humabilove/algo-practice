# BOJ 2745

import sys

def main():
    input = sys.stdin.readline
    
    NB = list(map(str, input().split()))
    N_list = list(NB[0].strip()) # ex) ZZZZZ -> ['Z', 'Z', 'Z', 'Z', 'Z']
    N_list.reverse() # 숫자 뒤집기 (for 문의 인덱스를 사용하기 편하게 하기 위함)
    B = int(NB[1]) # ex) 36
    num_len = len(N_list)
    
    ans = 0
    
    for i in range(num_len):
        num = ord(N_list[i])
        
        if num < 60:
            # 0부터 9이면 48~57로 바뀌고
            num -= 48
        else:
            # A부터 Z이면 65~90으로 바뀌기 때문
            # A부터 10으로 바꿔줘야함
            num -= 55

        ans += num * (B**i)
    
    print(ans)
    
if __name__ == "__main__":
    main()
