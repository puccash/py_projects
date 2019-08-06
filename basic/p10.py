# 반복문
# for
a = [1,2,3,4,5]
b = {'name':'수호랑',
    'addr':'수영'
}
c = (1,3,5,7,9)

# for ~ each 스타일만 지원
for item in a :
    # pass
    # 리스트를 for문으로 돌리면, 멤버를 하나씩 추출한다
    print(item)

for item in c :
    # 튜플 형식도 리스트 형식과 동일하게 추출된다
    print(item)

for item in b :
    # 딕셔너리 형식. 기본형식에서는 키 값이 먼저 추출된다.
    print(item)
for key in b :
    # 값을 추출하기 위해서는 인덱싱을 사용해준다.
    print(key, b[key])

d = [(1,2),(3,4),(5,6)]
# for item in d :
    # print(item)
    # 듀플은 변수로 사용할때, 멤버수와 동수로 변수를 나열하면, 순차적으로 작동한다
for i,j in d :
    print(i,j)
# 딕셔너리에서 만약, 인덱스를 추출하고자 한다면?
for i in enumerate(b) :
    print(b)
    # 인덱스가 없는데, 사용하고자 할때 사용하는 함수 : enumerate
for idx, key in enumerate(b) :
    print(idx, key)
# 연속수 만드는 내장함수 : range()
# 0 <= n < 3 
for n in range(3) :     # 3 : 경계값
    print(n)
# 1 <= n < 4
for n in range(1,4) :   # 1 : 시작값, 4 : 경계값  
    print(n)
# 1 <= n < 11 (간격 : by = 2)
for n in range(1,11,2) : # (시작값, 경계값, 간격)
    print(n)
# 3 ~ 7 구구단 구현
# 형식 : 3x1=3,
for a in range(3,8) :
    for b in range(1,11) :
        print(a*b, end=" ")
    print(' ')

# 곱의 결과의 자리수는 최대 2자리. 1자리 값인 경우, 좌측정렬로 표현
# 강사님 풀이 -> 포멧팅 사용.
for i in range(3,8) :
    for j in range(1,10) :
        # print( '3X1=3'.format() )
        # print ( '{}X{}={}'.format(i,j,i*j) )      # 계산식 형식의 정렬
        print ( '{0}X{1}={2:>2}'.format(i,j,i*j) )  # 자릿수 정렬

# 위의 결과물을 리스트화 하고자 한다면?
results = list()
for i in range(3,8) :
    for j in range(1,10) :
        # print ( '{0}X{1}={2:>2}'.format(i,j,i*j) )
        # 리스트에 생성된 문자열을 멤버로 추가
        results.append ( '{0}X{1}={2:>2}'.format(i,j,i*j) )
print(results)
# 한줄로 줄인다면?  >> 리스트 형식은 [] 부여 후 [] 안에 들어갈 내용을 추가한다.
results2 = ['{0}X{1}={2:>2}'.format(i,j,i*j)    # 1. 결과 형식 작성
    for i in range(3,8)                         # 2. 1번에서 i가 무엇인지 정의
    for j in range(1,10)]                       # 3. 1번에서 j가 무엇인지 정의
print(results2)                                 # 4. 결과값 도출
# 한줄로 코드를 줄인다 = 리스트 내포, 딕셔너리 내포, 시퀀스 타입은 모두 가능


