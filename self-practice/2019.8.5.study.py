# 수치형(숫자형) : 정수, 진법, 부동소수, ...
#정수
a=10
print(a)
#실수(소수점 포함)
a=2.5
print(a)
print(type(a))
#컴퓨터식 지수 표현 방법
a=4.5E10    # 4.5 곱하기 10(e)의 10승
print(a)
a=4.5e-10   # 4.5 곱하기 e의 -10승
print(a)
#8진수
a = 0o16
print(a)
#16진수
a = 0x10
print(a)
#사칙연산
a=5
b=7
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(b//a) # 나누기 후, 몫 반환
print(b%a)  # 나누기 후, 나머지 반환

# 문자열
a='Hi'
b='coco'
c=' '
print(a)
print(b)
print(a+c+b)
print(b+c+a)
d="Music is my life"
print(d)
e='''"I'am lionking"'''
print(e)
f='python\'s likes apple'
print(f)
g="\"v-tol is exciting!\ b.d"
print(g)
h='''
Baby shark~
Mommy shark~
Daddy shark~
'''
print(h)
i="baby\n shark"
print(i)
j='tiger'
print(j*2)
k='bear'
print(j+k)
print('ABO blood'*10)
print(k, len(k), type(k))
l = "Life is too short, so we have to fun life"
print(l,len(l))
print(l[0],l[-1])
print(l[-8:])
m = '20190806Storm'
date = m[:8]
print(date)
weather = m[8:]
print(weather)