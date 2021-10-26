# 11
# 입력한 값을 원하는 형태로 계산하거나 처리하기 위해서는 입력한 값이 어떤 데이터(정수, 문자, 실수, 문자열 등)인지 명확히 구분
f = input()
f = float(f)
print(f)

# 12
a = input()
b = input()
print(a)
print(b)

# 13
a = input()
b = input()
print(b)
print(a)

# 14
f = input()
f = float(f)
print(f)
print(f)
print(f)

# 15
# input()은 한 줄 단위로 입력을 받음
# 공백을 기준으로 입력된 값들을 나누어(split) 자름
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 16
a, b = input().split()
print(b, a)

# 17
# python 언어에서는 문자/정수/실수/문자열 등 특별한 구분이 없이도 원하는 변수에 저장시켜 출력
s = input()
print(s, s, s)

# 18
# sep 는 분류기호(seperator)
h, m = input().split(':')
print(h, m, sep=':')

# 19
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20
n = input()
n = n.replace('-','')
print(n)