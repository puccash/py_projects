# 단일 데이터(단일 타입)
# 문자열(연속이지만, 이쪽으로도 분류한다)
# 표기법
# '....' , "....." , '''.....''' , """......."""
# '''....''' , """....."""  용도 : 여러줄 표현, 구조유지, 여러줄 주석용
a = 'hi'
print(a)
a = "hi"
print(a)

# 혼용 표현
a = 'abcd"KKK"efg'
print(a)

# 이스케이프 문자로 동일 기호를 내부에서 사용 가능
a = 'abcd\kkk\efg'
print(a)

# 여러줄 사용
a = ''' asdfs
safwwd
erw2fs2
4r32ed
'''
print(a)

"""
여러줄 주석
"""

# 문자열 더하기 (이어 붙이기)  <--> 문자열 안의 문자열(포멧팅)
a = 'hello'
b = 'mint'
print(a+b)

# 문자열 반복
print('1'*10)

# 인덱싱 : Indexing : 문자열에서 특정 문자를 획득하는 방식 >> 차원 축소
# 문법 : 변수명[인덱스(정방향 or 역방향)]  >> 방향의 기준은 가까운 쪽에서 시작
a = '0123456789'
# a에서 2를 출력하기
print(a[2])
print(a[-8]) # : 뒷쪽에서부터는 멀기 때문에 가까운쪽에서 해결할 것

# 슬라이싱 : 데이터에서 범위에 해당되는 데이터를 획득 >> 차원 유지
# 문법 : 변수[ 시작인덱스:끝인덱스:step ]   >> step : cut 간격, 생략시 defalut 값 1
# a를 카피한다
print(a[:])
# 1 부터 8 까지 출력하기
# 뒷쪽의 경계값은 포함되지 않는다.
print(a[-1],a[1])
# a <= < b
print(a[1:-1])
print(a[1:-1:3])

url = 'https://cdn.clien.net/web/api/file/F01/2475133/20067898062c482492e.JPG'
# 위의 이러한 문자열의 파일명 추출, 도메인 추출 등등 사용가능 
print(a[:2],a[-2:])

# 멤버함수 (문자열)
a = '0123456789'
# 문자열 내의 특정 문자 갯수 파악하기
print('a라는 문자열의 3의 갯수', a.count('3'))
print('a라는 문자열의 -1의 갯수', a.count('-1')) # 값이 없으면 0 이 나타난다
print('a라는 문자열의 A의 갯수', a.count('A'))
# a라는 문자열에 "A"라는 문자가 존재하는가?
print(a.count('A')>0)
print(a.index('2'))
# 에러 및 없는 문자는 예외처리가 필요하다.
# print(a.index('A'))
print(a.find('2'))
print(a.find('A'))
# 문자열 내에서 문자열 찾기는 count(), find()를 사용할 것.
b = ','
# 조인
print(b.join(a))
# 분해
print(b.join(a).split(b))
# 공백제거
a = '         sdsd           '
print('[%s]'%a.rstrip())
print('[%s]'%a.lstrip())
print('[%s]'%a.strip())
# 가운데 공백 제거 >> 정규식

# 대소문자
a = 'asdasASDF가나다라1234!@#$'
print(a.upper())
print(a.lower())

# 조합 사용 
url = 'https://cdn.clien.net/web/api/file/F01/2475133/20067898062c482492e.JPG'
# >> image.png (or jpg) 라는 문자열을 획득. 리스트 인덱싱 사용
# 단 상수값은 사용하지 않는다.
# 이미지 값을 구해가는 과정
tmp = url.split('/')
print(url.split('/'))
print(url.split('/')[-1] )
print(tmp)
print(len(tmp))
print(tmp[-1])
print(tmp[len(tmp)-1])
print(url.count('/'))
print(url.split('/')[url.count('/')])

# 포멧팅
a=1
b=2
# x+y=z 형식으로 출력하기
print('%d+%d=%d' % (a,b,a+b) )
# %s를 사용하는 경우 : 데이터가 문자열일떼, 데이터의 타입을 모를 때.
print('%s+%s=%s' % (a,b,a+b) )
print('%d/%d=%f' % (a,b,a/b) )
print('%d/%d=%s' % (a,b,a/b) )
# .format() 처리
print( '{}+{}={}'.format(a, b, a+b) )
print( '{0}+{1}={2}'.format(a,b,a+b))
print( '{1}+{0}={2}'.format(a, b, a+b) )

# format 의 파라미터를 모두 다 쓸 필요는 없다.
print( '{1}+{1}={1}'.format(a, b, a+b) )
print( '{0}+{1}={result}'.format(a, b, result=a+b) )
# print(result)  >>> Error
# 포멧팅, 자리수 체크
print('[%s]'%'12345')
# 20칸에 배치 시,
print('[%20s]'%'12345')   # 앞 쪽 정렬
print('[%-20s]'%'12345')  # 뒷 쪽 정렬
print('[%0.2f]'%3.145625) # 반올림  >> 수치 변경
print('[%10.2f]'%3.145625)
print('[%10.2f]'%3.145625)
# 뒷쪽 정렬
print('[%10s]'%'12345')
# 치환식
a = 'abc()efg'.format('k')
print(a)
# 자릿수 10개
a = 'abc{0:<10}efg'.format('k')
print(a)
a = 'abc{0:>10}efg'.format('k')
print(a)
# 짝수칸일 경우, 앞쪽으로 센터 위치
a = 'abc{0:^10}efg'.format('k')
print(a)
# *로 빈칸 채우기
a = 'abc{0:*^10}efg'.format('K')
print( a )