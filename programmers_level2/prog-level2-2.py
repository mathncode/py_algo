# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

from collections import deque

def solution(priorities, location):
    # location에 해당하는 priorities리스트의 원소를 기억하기 위해 ind 생성 0부터 숫자를 채워 넣기
    ind = []
    for i in range(len(priorities)):    
        ind.append(i)   

    p = deque(priorities)
    ind = deque(ind)

    count = 0
    while location in ind:
        if p[0] == max(p):
            p.popleft()
            ind.popleft()
            count += 1
        else:
            c = p[0]
            d = ind[0]
            p.popleft()
            ind.popleft()
            p.append(c)
            ind.append(d)    
    
    return count