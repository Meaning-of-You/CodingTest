# 61
# | 은 파이프(pipe)연산자
a, b = input().split()
print(int(a)|int(b))

# 62
# ^은 수학식에서 거듭제곱(power)을 나타내는 기호와 모양은 같지만, C언어에서는 전혀 다른 배타적 논리합(xor, 서로 다를 때 1)의 의미
a, b = input().split()
print(int(a)^int(b))

# 63
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# x : C의 평가 결과가 True 일 때 사용할 값
# y : C의 평가 결과가 True 가 아닐 때 사용할 값
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 64
# ex) (a if a>b else b) if ((a if a>b else b)>c) else c
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = a if a <= ((b if (b<=c) else c)) else ((b if (b<=c) else c))
print(int(d))

# 65
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print(a)
if b%2 == 0:
    print(b)
if c%2 == 0:
    print(c)

# 66
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print("even")
else:
    print("odd")
if b%2 == 0:
    print("even")
else:
    print("odd")
if c%2 == 0:
    print("even")
else:
    print("odd")

# 67
a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
else:
    if a%2==0:
        print('C')
    else:
        print('D')

# 68
s = int(input())
if s >= 90:
    print('A')
elif s >= 70:
    print('B')
elif s >= 40:
    print('C')
else:
    print('D')

# 69
s = input()
if s == 'A':
    print('best!!!')
elif s == 'B':
    print('good!!')
elif s == 'C':
    print('run!')
elif s == 'D':
    print('slowly~')
else:
    print('what?')

# 70
s = int(input())
if s >= 3 and s <= 5:
    print('spring')
elif s >= 6 and s <=8:
    print('summer')
elif s >=9 and s <= 11:
    print('fall')
else:
    print('winter')

a = int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")