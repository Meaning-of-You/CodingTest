# 51
# 비교/관계연산자 != 는 왼쪽의 계산 결과값이 오른쪽의 계산 결과값이 서로 다른 경우 True(참)로 계산하고, 그 외의 경우에는 False(거짓)로 계산
a, b = input().split()
print(a!=b)

# 52
# bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력
# 식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)
n = int(input())
print(bool(n))

# 53
# 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능
# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용
a = bool(int(input()))
print(not a)

# 54
# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 나머지 경우는 False 로 계산
# 러한 논리연산을 AND 연산(boolean AND)이라고도 부르고, · 으로 표시하거나 생략하며, 집합 기호 ∩(교집합, intersection)로 표시
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 55
# or 예약어는 주어진 두 불 값 중에서 하나라도 True 이면 True 로 계산하고, 나머지 경우는 False 로 계산
# 이러한 논리연산을 OR 연산(boolean OR)이라고도 부르고, + 로 표시하거나, 집합 기호 ∪(합집합, union)로 표시
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 56
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))

# 57
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a) and (not b))

# 58
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((not a and not b))

# 59
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드)
# 비트단위(bitwise) 연산자는, ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)
a = int(input())
print(~a)

# 60
# 비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드)
a, b = input().split()
print(int(a) & int(b))