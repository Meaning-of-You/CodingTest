# 31
# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능
c = int(input())
print(chr(c))

# 32
# 단항(unary) 연산자인 -(negative)를 변수 앞에 붙이면 부호가 반대인 값이 됨
n = int(input())
print(-n)

# 33
s = ord(input())
print(chr(s+1))

# 34
# 수 - 수는 차(subtraction)가 계산
a, b = input().split()
c = int(a)-int(b)
print(c)

# 35
# 수 * 수는 곱(multiplication)이 계산
f1, f2 = input().split()
m = float(f1)*float(f2)
print(m)

# 36
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 줌
w, n = input().split()
print(w*int(n))

# 37
n = input()
s = input()
print(int(n)*s)

# 38
# 거듭제곱을 계산하는 연산자(**)
a, b = input().split()
c = int(a)**int(b)
print(c)

# 39
f1, f2 = input().split()
c = float(f1)**float(f2)
print(c)

# 40
# 나눈 몫을 계산하는 연산자(//, floor division)
a, b = input().split()
c = int(a)//int(b)
print(c)