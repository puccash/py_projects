# 조건문
# while

a = [1,2,3,4,5]
while len(a) > 0:   # 현 상태에서는 무한반복이 된다
    print(a.pop( )) # pop : 배열의 맨 뒷자리부터 하나씩 추출하여 리턴작용한다 >> 멤버 수 감소

# 조건문은 시퀀스타입을 자체 변수를 사용하여 활용 가능
# 로직은 동일 하게, 조건문을 간결하게 구현한다면?
# 멤버가 모두 비워지면, [] 사용 >> 조건문에 insert 하면 >> false 된다.
# >> 멤버가 있는지 없는지 check >> a 만 넣어서 조건문에서 check
# while a ::
    
# 반복문이 정상적으로 작동하는지 알게 하는 표현
while a :
    print(a.pop())
else : 
    print('반복문의 중간 멈춤없이 반복, 루프 ok')

while a :
    print(a.pop())
    if len(a) == 2:
        break
else : 
    print('반복문의 중간 멈춤없이 반복, 루프 ok')
