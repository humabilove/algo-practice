# Baekjoon Solutions
# 백준 파이썬 템플릿 자동 생성기 (`boj` 명령)

터미널에서 문제 번호만 입력하면 자동으로

* `BOJ_문제번호.py` 파일을 만들고
* 안에 기본 템플릿 코드까지 채워주는

작업을 자동화한 설정 정리 📌

---

## 1. 개요

이 레포지토리에서는 백준 문제를 파이썬으로 풀 때, 다음을 자동으로 처리한다.

* `boj 1000` → 현재 폴더에 `BOJ_1000.py` 생성
* `boj io 1000` → `input_output_arithmetic_operations/BOJ_1000.py` 생성
* `boj cond 1330` → `conditional_statement/BOJ_1330.py` 생성
* 파일 맨 위에는 항상 `# BOJ <문제번호>` 주석이 자동으로 들어감
* 파일 내부에는 자주 쓰는 파이썬 템플릿이 자동으로 들어감

---

## 2. 사전 조건

* macOS
* 기본 쉘: `zsh`
* VSCode 사용 (선택 사항, 있으면 편함)
* 레포지토리 루트 예시 구조:

```bash
algo-practice/
  conditional_statement/
  input_output_arithmetic_operations/
  py-general.py
  py-algo.py
  README.md
```

---

## 3. `boj` 함수 설정 방법

### 3-1. zsh 설정 파일 열기

터미널에서:

```bash
nano ~/.zshrc
```

또는 VSCode:

```bash
code ~/.zshrc
```

### 3-2. 파일 맨 아래에 아래 함수 추가

```bash
boj() {
  # 사용법 안내
  if [ -z "$1" ]; then
    echo "사용법:"
    echo "  boj <문제번호>"
    echo "  boj <카테고리> <문제번호>"
    echo "예시: boj 1000 / boj io 1000 / boj cond 1330"
    return 1
  fi

  local dir="."
  local problem=""
  
  # 인자가 1개면: 현재 디렉토리에 생성 (예: boj 1000)
  if [ $# -eq 1 ]; then
    problem="$1"
  
  # 인자가 2개면: 카테고리/문제번호 (예: boj io 1000)
  elif [ $# -eq 2 ]; then
    local category="$1"
    problem="$2"

    # 카테고리별 폴더 매핑
    case "$category" in
      io)
        dir="input_output_arithmetic_operations"
        ;;
      cond)
        dir="conditional_statement"
        ;;
      *)
        # 위에서 지정한 것 외의 카테고리는 폴더 이름을 그대로 사용
        # 예: boj dp 1000 -> dp/BOJ_1000.py
        dir="$category"
        ;;
    esac
  else
    echo "인자 개수가 잘못되었습니다."
    echo "사용법: boj <문제번호> 또는 boj <카테고리> <문제번호>"
    return 1
  fi

  # 카테고리 폴더 없으면 생성
  mkdir -p "$dir"

  local filename="BOJ_${problem}.py"
  local filepath="${dir}/${filename}"

  if [ -e "$filepath" ]; then
    echo "$filepath 이미 존재합니다."
    return 1
  fi

  # 템플릿 파일 생성
  cat > "$filepath" << EOF
# BOJ ${problem}

import sys

def main():
    input = sys.stdin.readline
    
    # TODO: 여기부터 코드 작성


if __name__ == "__main__":
    main()
EOF

  echo "생성 완료: $filepath"

  # 생성 후 바로 VSCode로 열고 싶으면 아래 줄 주석 해제
  # code "$filepath"
}
```

### 3-3. 변경 내용 적용

```bash
source ~/.zshrc
```

또는 터미널을 껐다 다시 켠다.

---

## 4. 사용법

### 4-1. 현재 디렉토리에 파일 생성

예시: 입출력/사칙연산 폴더에서 직접 생성할 때

```bash
cd ~/.../algo-practice/input_output_arithmetic_operations

boj 1000
```

→ 결과:

* 현재 폴더(= `input_output_arithmetic_operations`)에 `BOJ_1000.py` 생성

파일 내용 예시:

```python
# BOJ 1000

import sys

def main():
    input = sys.stdin.readline
    
    # TODO: 여기부터 코드 작성


if __name__ == "__main__":
    main()
```

### 4-2. 레포 루트에서 카테고리 + 문제 번호로 생성

레포지토리 루트 (`algo-practice`) 에서:

#### 입출력/사칙연산 (`io`)

```bash
cd ~/.../algo-practice

boj io 1000
```

→ `input_output_arithmetic_operations/BOJ_1000.py` 생성

#### 조건문 (`cond`)

```bash
boj cond 1330
```

→ `conditional_statement/BOJ_1330.py` 생성

#### 새로운 카테고리 생성

```bash
boj loop 2739
```

→ `loop/BOJ_2739.py` 생성
→ `loop` 폴더가 없으면 자동으로 생성

---

## 5. 템플릿 코드 형식

자동으로 생성되는 파일의 기본 내용:

```python
# BOJ <문제번호>

import sys

def main():
    input = sys.stdin.readline
    
    # TODO: 여기부터 코드 작성


if __name__ == "__main__":
    main()
```

* 맨 위: `# BOJ <문제번호>` 주석으로 문제 번호 기록
* `import sys` + `input = sys.stdin.readline` 으로 빠른 입력 세팅
* `main()` 함수 안에서 문제 풀이 작성
* 마지막에 표준적인 파이썬 엔트리 포인트 사용

---

## 6. VSCode와 연동 (선택)

파일 생성 후 바로 VSCode로 열고 싶다면:

1. VSCode에서 `code` 명령 사용 가능하게 설정

   * VSCode → Command Palette (`Cmd + Shift + P`)
   * `Shell Command: Install 'code' command in PATH` 실행

2. `~/.zshrc` 안의 `boj` 함수 마지막 부분에서

   ```bash
   # code "$filepath"
   ```

   이 줄의 `#`를 지워서:

   ```bash
   code "$filepath"
   ```

   로 변경.

이제:

```bash
boj io 1000
```

을 실행하면

* 템플릿 파일 생성 +
* VSCode에서 해당 파일 자동으로 열림

---

## 7. 카테고리 추가/수정 방법

새로운 카테고리를 추가하고 싶으면, `boj` 함수의 `case` 부분만 수정하면 된다.

예시:

```bash
    case "$category" in
      io)
        dir="input_output_arithmetic_operations"
        ;;
      cond)
        dir="conditional_statement"
        ;;
      dp)
        dir="dynamic_programming"
        ;;
      *)
        dir="$category"
        ;;
    esac
```

이렇게 하면:

```bash
boj dp 1463
```

→ `dynamic_programming/BOJ_1463.py` 생성

---

## 8. 자주 쓸 명령 예시 모음

```bash
# 레포 루트로 이동
cd ~/.../algo-practice

# 입출력/사칙연산 문제
boj io 1000
boj io 1001
boj io 10998

# 조건문 문제
boj cond 1330
boj cond 9498

# 새로운 카테고리 만들면서 풀기
boj loop 2739      # 구구단
boj while 10951    # while문 카테고리 등
```
