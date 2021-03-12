# https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

import math
from itertools import permutations

# 소수 찾기
def solution(numbers):
    def prime_number(x):
        if x == 0 or x == 1: 
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True        

    # 순열 이용해서 모든 경우의 수 생성 후 정수로 변환 
    num = []
    for i in range(len(numbers)):
        p = list(permutations(numbers, i+1))
        for i in p:
            b = int(''.join(i))
            num.append(b)

    num_set = set(num)  # 중복을 제거하기 위해 집합으로 변환
    
    count = 0    
    for i in num_set:  # 집합 안에서 소수를 찾아 개수 세기
        if prime_number(i):
            count += 1
    
    return count