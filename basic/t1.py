# 문자열을 숫자(정수)로 변환이 가능한지 check하는 내용 >> 조사
A = [
''
,'1'
,'1.1'
,'A'
,'a'
,'@'
,'가'
]

for data in A :
    print(data, data.isalpha(), data.isdecimal(), data.isdigit(), data.isnumeric())

# 외장 함수
    # 외장함수는 항상 이를 가져오는 절차인 import가 존재한다 (필수 사항)
# 모듈을 가져와서 내부에 존재하는 함수를 사용하는 case
import random
for n in range(10) :
    # 시작값 <= 난수 <= 끝 값
    # print( random.randint(1,3) )
    print( random.randint(0,99) )

