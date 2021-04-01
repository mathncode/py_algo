# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

# 아이디어와 풀이는 https://mathncode.tistory.com/37
def solution(n):
    a = ''
    while n > 0:
        r = n % 3
        q = n // 3

        if r == 0:      # 나머지가 0이면 자릿수 변경. 올라간 자릿수를 1낮추고, 3대신 4로 바꾼다.
            r = 4
            q -= 1

        a += str(r)
        n = q

    answer = a[::-1]
    return answer