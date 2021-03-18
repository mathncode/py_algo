# https://programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이

def solution(n):
    arr = [[0]*n for _ in range(n)]
    dx = [1, 0, -1] # d, D
    dy = [0, 1, -1] # r, D
    t = ['d', 'r', 'D'] # 수를 채우는 방향은 아래, 오른, 대각의 반복

    # n번 아래, n-1번 오른, n-2번 대각, n-3번 아래... 맞춰서 리스트에 t, r, D 해당 회수 만큼 담기
    c = 0
    m = []
    for i in reversed(range(1, n + 1)):
        for _ in range(i):
            m.append(t[c % 3])
        c += 1
    
    x, y = -1, 0 #시작점
    num = 1
    # 리스트 m에 담긴 원소에 맞춰 이동하면서 숫자 넣기
    for p in m:
        for i in range(len(t)):
            if p == t[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        arr[nx][ny] = num
        x = nx
        y = ny
        num += 1
    
    answer = []
    # 리스트 m에서 0을 제외한 원소만 새로운 리스트에 담기
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])

    return answer