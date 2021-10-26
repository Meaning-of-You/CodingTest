# 41
# 나눈 나머지를 계산하는 연산자(%, remainder)
a, b = input().split()
print(int(a)%int(b))

# 42
# format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 줌
a = float(input())
print(format(a, '.2f'))

# 43
# 나눗셈(division)을 계산하는 연산자(/)
f1, f2 = input().split()
n = float(f1)/float(f2)
print(format(n, '.3f'))

# 44
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, '.2f'))

# 45
# python 프로그래밍을 처음 배울 때 좋은 습관(단계)
# 1. 입력된 문자열을 정확하게 잘라낸다.(공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)
# 2. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. (정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)
# 3. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 변수를 이용해 계산을 한다.
# 4. 원하는 결과 값을 필요한 형태로 만들어 출력한다.(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)
a, b, c = input().split()
print(int(a)+int(b)+int(c), format((int(a)+int(b)+int(c))/3, '.2f'))

# 46
# 수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용
# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고, 가장 오른쪽에 있는 1비트는 사라짐
a = int(input())
print(a<<1)

# 47
a, b = input().split()
print(int(a)<<int(b))

# 48
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용
# 왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고, 그 외의 경우에는 False(거짓)로 계산
# <, >, <=, >=, ==(같다), !=(다르다) 
a, b = input().split()
print(int(a)<int(b))

# 49
# 비교/관계연산자 == (equal sign 2개)는 왼쪽의 계산 결과값과 오른쪽의 계산 결과값이 같은 경우 True(참)로 계산하고, 그 외의 경우에는 False(거짓)로 계산
a, b = input().split()
print(int(a)==int(b))

# 50
# 비교/관계연산자 <= 는 오른쪽의 계산 결과값이 왼쪽의 계산 결과값보다 크거나 같은 경우 True(참)로 계산하고, 그 외의 경우에는 False(거짓)로 계산
a, b = input().split()
print(int(a)<=int(b))