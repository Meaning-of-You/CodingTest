# 21
s = input()
for i in range(0, len(s)):
    print(s[i])

# 22
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미
s = input()
print(s[0:2], s[2:4], s[4:6])

# 23
h, m, s = input().split(':')
print(m)

# 24
# 공백문자로 구분된 문장에서 단어를 잘라내기 위해서는 공백문자(' ')를 기준으로 자르면 됨
w1, w2 = input().split()
s = w1+w2
print(s)

# 25
# 입력되는 값은 기본적으로 문자열로 인식
# 숫자로 구성된 문자열이나 실수를 정수(integer) 값으로 바꾸기 위해서는 int( )를 사용
a, b = input().split()
s = int(a)+int(b)
print(s)

# 26
# 숫자로 구성된 문자열이나 정수를 실수(real number) 값으로 바꾸기 위해서는 float( )를 사용
a = float(input())
b = float(input())
s = a+b
print(s)

# 27
# 0진수 형태로 입력받고 %x로 출력하면 16진수(hexadecimal) 소문자로 출력
a = int(input())
print('%x'%a)

# 28
# 10진수 형태로 입력받고 %X로 출력하면 16진수(hexadecimal) 대문자로 출력
a = int(input())
print('%X' %a) 

# 29
# %o로 출력하면 8진수(octal) 문자열로 출력
a = int(input(),16)
print('%o' %a)

# 30
# ord( )는 어떤 문자의 순서 위치(ordinal position) 값을 의미
# ord(c) : 문자 c 를 10진수로 변환한 값 
a = ord(input())
print(a)