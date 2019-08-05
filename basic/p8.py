# 조건문, 반복문
# 내장함수 input() : 터미널을 통해 사용자의 입력을 받는다.
# 문자열을 리턴하고, 인자를 넣으면 프롬포트로 사용된다.

price = int(input('막국수는 얼마인가요?'))   # 동기식 진행.(값을 부여하지 않으면 코드 진행 불가)
print(price)

# 조건문, 반복문 등 문장의 끝을 의미하고, 코드블럭을 시작하라는 의미.
if price >6000 :
    # pass 의미 : statement 최소 1줄에 대한 조건 만족. 아무것도 하지 않는 장소. >> 틀 만들기 용도
    print('꿀꺽')
    pass
elif price == 6000 :
    print('할짝')
    pass
else:
    print('옴뇽뇽')
    pass