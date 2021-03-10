# https://programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형

import math

def solution(w,h):
    # 최대공약수를 이용하여 사용 불가능한 사각형의 패턴이 생기는 최소 단위 직사각형의 변의 길이를 구합니다.
    # 예시에서는 가로 2, 세로 3이며, 번개 모양의 정사각형 4개를 사용 못합니다. 
    # 밑에 반복문에서 연산 횟수를 줄이기 위해 가로와 세로 중 큰 값을 m, 작은 값을 n
    g = math.gcd(w, h)
    m = max(w//g, h//g)
    n = min(w//g, h//g)
    
    sum_rec = 0
    
    # 반복문은 최소 단위 직사각형에서 사용 가능한 정사각형 개수를 구합니다.
    for i in range(1, n):
        c = int(m/n*i)
        sum_rec += c
    
    # 사용 못하는 정사각형의 개수를 구합니다.
    useless_rec = (m*n - sum_rec*2)*g
    
    # 사용가능한 정사각형의 개수를 구합니다.
    answer = w * h - useless_rec
    
    return answer