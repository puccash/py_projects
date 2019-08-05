'''
> 딕셔너리 : {}
순서 없음, 키 : 값, 키는 중복되면 X, 값 중복은 가능
>> 테이블 상의 한개의 row, json 객체, js의 객체와 동일
'''
# 아래 첫번째 스타일을 주로 사용
dic = {}
print(dic, len(dic), type(dic))

dic = dict()
print(dic, len(dic), type(dic))

# 키를 통해서 값을 직관적으로 이해할 수 있다.
dic = {
    'name':'호랑이',
    'age':100
}
print(dic, len(dic), type(dic))

# 인덱싱 : 순서가 없으므로, 데이터를 특정할 수 있는 키 값을 사용
print(dic['name'])
#데이터 추가. 키는 뭐든지 올 수 있다. 여기서 2는 인덱스가 아닌 키를 의미한다.
dic[2]='hello'
print(dic, len(dic), type(dic))

print( dic.keys())
print( dic.values())
# 키 조사
print( 'name' in dic)
# for 문 사용 >> 추후 예정