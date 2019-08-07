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
# 2019.8.5
n='20190806Thunder'
year = n[:4]
month = n[4:6]
date = n[6:8]
weather = n[8:]
print(year, month, date, weather)

# mont 라는 문자열을 mint 로 변환하기
o = "mont"
print(o[1])
# o[1] = i    print(o)    > 에러. 연산 불가
# 문자열을 슬라이싱 하여 재조합하기.
o1 = o[:1]
o2 = o[2:]
print( o1 + 'i' + o2 )

# 문자열 포멧팅
'''
문자열 포멧 코드
%s : 문자열(string)
%c : 문자 1개(character)
%d : 정수(integer)
%f : 부동소수(floating-point)
%o : 8진수
%x : 16wlstn
%% : 문자 % 그 자체 (n% 표현시 사용)
'''

# List 자료형 = []
# 리스트명 = [요소, 요소, 요소 ...]
la = [1,2,3]
lb = ['a','b','c']
lc = [1,2,'a','b']
ld = [1,2,['a','b',3]]
print(la, lb, lc, ld)
aa = list()
print(aa)
print(la[1], lb[1], lc[3])
print(ld[2])
#ld 에서 요소 b 추출하기  >> 인덱싱을 2회 하여, 차원 축소 및 추출
print(ld[2][1])
#리스트 연산
la1 = [1,2]
la2 = [3,4,5]
print(la1+la2)
print(la2*2)
print(len(la1))
#리스트 요소 치환
la2[1] = 9
print(la2)
