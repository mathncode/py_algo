# https://programmers.co.kr/learn/courses/30/lessons/12953
# N개의 최소공배수

# 가장 큰 수를 찾아 큰 수의 배수 중 최소공배수가 되는지 확인 
def solution(arr):
    answer = 0
    m = max(arr)
    lcd = 0
    n = 1
    
    while True:
        lcd = m * n
        for i in arr:
            if lcd % i != 0:
                break
        else:
            break    
        n += 1
        
    answer = lcd
    return answer


# 세 수 a, b, c 에 대해 a, b의 최대공약수를 e라 하면 e와 c의 최대공약수 f가 세 수 a, b, c의 최대공약수이다.
# 최소공배수도 마찬가지 방법으로 구할 수 있다.
# 두 수 a, b의 최소공배수 lcd = ab / gcd 이다. 
def solution1(arr):
    # 유클리드 호제법으로 최대공약수 구하는 함수
    def gcdiv(a, b):
        n = max(a, b)
        q = min(a, b)
        while n > 0:
            r = n % q
            if r == 0:
                return q
            n = q
            q = r

    # 최소공배수 구하기    
    lcd = arr[0]
    for i in range(1, len(arr)):       
        lcd = lcd * arr[i] // gcdiv(lcd, arr[i])
    
    return lcd 