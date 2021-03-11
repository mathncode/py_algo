# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    b = deque([0]*bridge_length)    # 다리 길이만큼 0으로 찬 큐를 만듭니다.
    t = deque(truck_weights)
    
    sum_weight = 0    # 다리 위 트럭들의 무게 합
    total_time = 0
    
    while True:
        # 컨베이어 벨트 처럼 0을 넣고 빼고 하되, 조건에 맞을 때만 트럭이 올라간다.
        out = b.popleft()
        sum_weight -= out
        
        # 조건에 맞으면 트럭이, 안맞으면 0이 올라갑니다.
        if sum_weight + t[0] <= weight:
            b.append(t[0])
            sum_weight += t[0]
            t.popleft()
        else:
            b.append(0)
    
        total_time += 1
    
        if len(t) == 0:
            # 다리에 막 진입한 마지막 트럭은 다리길이 만큼 시간이 지나야 건넌다.
            total_time += bridge_length
            break
    
    answer = total_time
    return answer

# 첫 if문에서 sum_weight 대신에 sum(b)를 이용해 다리 위 무게 합을 매번 구하게 했더니 시간 초과가 났다.
# 반복문이 돌 때마다 sum(iteralbe)이 매번 실행되는 건 상당한 시간을 소비하는 것 같다.   