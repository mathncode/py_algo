# 튜플을 원소로 가지는 리스트를 람다식을 이용해서 정렬
n = int(input())

array = []

for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x: x[1])

for x in array:
  print(x[0], end = ' ')