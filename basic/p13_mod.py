# p14.py 모듈 가져오기 진행 중, p13_mod 생성

# Class
# 파이썬에서 자기 자신 객체를 지칭하는 키워드 : self
# self >> python , objective-c
# this >> java, js, 대부분의 언어체계
class Person :
    '''
    멤버변수
    >> 초기화해주지 않으면 에러가 난다
    '''
    name   = None
    age    = 0
    weight = 0
    
    '''
    멤버함수
    '''
    def eat(self, food) :
        print( '%s를 먹는다' % food)

    '''
    생성자
    >> 객체를 생성하고, 멤버변수를 초기화 하는 것이 목적
    '''
    def __init__(self, name, age, weight) :
        # 멤버변수 초기화
        # class 내부에서 멤버들에 접근할때, self.멤버(변수 or 함수)
        self.name   = name
        self.age    = age
        self.weight = weight
        # 부모 생성자 호출
        # return super().__init__( )
    
    '''
    객체를 설명하는 코드를 구현. 통상 문자열로 구성
    멤버 변수값이나 상태를 표현한 정보가 들어가면 ok.
    자바의 toStrin()의 맥락과 유사
    '''

    def __repr__(self):
        return '''
        name=%s age=%s weight=%s
        ''' % (self.name,self.age,self.weight)


# 상속
# 부모의 모든 것을 가진 상태로, 재 정의 할 수 있고, 추가 가능하다
class XMan(Person) :
    # 멤버 변수 추가
    abil = 100
    # 멤버 함수 추가
    def speed(self) :
        print('500km/h로 날아간다')
    # 재정의 : 내용 구성이 부모에 대비하여 달라진다. >> overriding
    def eat(self, food) :
        print('%s를 1초 만에 요리한다' % food)
    # 생성자
    def __init__(self, name, age, weight, abil) :
        super().__init__(name, age, weight)
        self.abil = abil

# 테스트 코드는 특정 조건을 만족할때만 수행되도록 구성
if __name__ == '__main__' :         # 파이썬 웹 의 시작점 코드에 항상 사용되는 것.
    obj = Person('수호랑',1,2)
    print(obj)
    obj.eat('1')

    mu = XMan('김종국', 200, 100, 85)
    mu.speed()
    mu.eat('건강식')
    print(mu)
    print('p13 : __name__', __name__)