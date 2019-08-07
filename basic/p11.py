# 함수
# function, method
# 반복작업 해소, 재활용성 높이고, 구조적 설계 >> 개발시간 단축

'''
def 함수명( [ 인자명, 인자명, 인자명, ... ] ) :
    statement
    [ return 값 ]
'''
# def 앞 자리에 static 등이 올 수 있다.

def add( x, y ) :
    return x+y

# 함수 사용
d = add(1,2)
print( d )

# 가변인자, 함수의 입력의 수가 가변인 경우
def add2( *args ) :
    print(args)
    # 인자로 전달된 데이터를 모두 더해서 리턴하기  >> 튜플(듀플)구조 >> 시퀀스 타입 >> 연속형 데이터 >> for문 사용
    sum = 0
    for arg in args :
        sum += arg
    return sum
print(add2(1,2))
print(add2(1,2,3))

# 가변인자로 전달된 데이터의 누적합과 누적곱을 계산하여 리턴하기
def mix( *args ) :
    print(args)
    sum, mul = (0,1)    # 정적 생성
    for arg in args :
        sum += arg
        mul *= arg
    # 리턴할 값이 여러개인 경우, 튜플로 리턴할 것
    return sum, mul
print(mix(1,2))
print(mix(1,2,3))
# 튜플 구조 특징 : 데이터를 받을 때, 반드시 순서를 확인할 것
a, b = mix(1,2,3,4,5,6,7)
print(a)
print(b)

# 리턴을 딕셔너리 구조로 시행 >> 순서 상관없이 하고 싶을 떼. 키 확인
def mix2( *args ) :
    print(args)
    sum, mul = (0,1)    
    for arg in args :
        sum += arg
        mul *= arg
    return { "sum":sum, "mul":mul }     # return {'키':값, '키':값}
print(mix2(1,2,3,4,5,6)['sum'])

# 로그함수
# debug 값이 True >> 노출된다. / debug 값이 false >> 숨겨진다

# 기본형태
# env_debug = True      
# def log(msg) :
#     print('-'*20)
#     print(msg)
#     print('-'*20)
# log('이것은 로그 메세지 출력 함수이다.')

env_debug = True
def log(msg) :
    if env_debug :
        print('-'*20)
        print(msg)
        print('-'*20)
log('이것은 로그 메세지 출력 함수이다.')

# 사용자 정의 함수 : 형태를 정의할 수 없음.  >> 프로젝트 시, 네이밍에 대한 정의가 필요
# 내장함수 : len(), type(), int(), str(), tuple(), dict(), list() ...
# 외장함수 : random.randit() , sys.exit() ...

# 함수 인자의 초기값 부여
# 초기값 인자들이 존재할때, 초기값이 없는 인자는 제일 앞쪽에 위치시켜야 한다
# def setPerson ( name='반다비', age=10, weight=85, score ) :   >> score 에러
def setPerson ( score, name='반다비', age=10, weight=85 ) :
    log( '%s %s %s %s' % (name,age,weight,score) )
setPerson(100)
setPerson(score=55)
# 기본값이 없는 함수의 파라미터는 반드시 값을 부여해야 한다
# setPerson(name='호랑이')

# 단순 나열시, 순서대로 인자를 전달한다
setPerson(1,2,3,4)

# 기본값이 부여된 파라미터들은 함수 호출 시, 순서에 상관없이 명시적으로 사용가능
setPerson(1, age=1004, name='호랑이')

log('수호랑')
log(msg='반다비')