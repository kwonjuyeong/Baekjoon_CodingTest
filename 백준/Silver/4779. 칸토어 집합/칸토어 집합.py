def cantor(n):
    if n == 0:
        return "-"  #n이 0이면 "-"을 반환하여 칸토어 집합의 기본 단계를 표현한다.
    else:
        prev = cantor(n - 1)  # 이전 단계의 칸토어 집합을 재귀 호출
        spaces = " " * (3 ** (n - 1))  # 현재 단계에서의 공백 계산 (3^(n-1)만큼의 공백)
        return prev + spaces + prev  # 현재 단계의 칸토어 집합을 구성하여 반환 ex) ---   ---

while True:
    try:
        N = int(input())  # 사용자로부터 정수 입력을 받음
        result = cantor(N)  # cantor 함수를 사용하여 칸토어 집합의 근사를 계산
        print(result)  # 결과를 출력
    except EOFError:  # EOF 에러: 파일의 끝에서 입력을 멈추기 때문에 예외 처리를 해준다.
        break