'''
연속데이터 (시퀀스 타입)
> 리스트 : []  >> js의 배열과 동일
순서가 존재, 값 중복 가능, 인덱스는 정방향 / 역방향 존재
'''
# 비어있는 리스트 생성
nums = []     # 정적 생성 
print(nums, len(nums), type(nums))
nums = list() # 동적 생성  >> 대량의 작업시 조금 더 안정적.
print(nums, len(nums), type(nums))

#정적 생성 : 일반적으로 문제는 없으나, 간혹 추가가 되지 않는 경우가 생긴다.
#           이러한 경우, 동적 생성으로 대체한다.
#           자료구조를 
nums = [1,3,5,7,9]
print(nums, len(nums), type(nums))
anis = ['dog','cat','bird']
print(anis, len(anis), type(anis))
# 리스트의 멤버들의 타입이 다르면 리스트를 구성할 수 없다? >> 무관하다
# 파이썬의 모든 것은 객체이므로, 멤버도 모두 객체 >> 주소를 가진다.
mix = [1,2,3,'dog','cat']
print(mix, len(mix), type(mix))
# 차원을 섞은 경우는? 멤버 중에 하나가 리스트인 경우.
multiTypeMatrix = [1,2,3,'dog','cat',['bird',100]]
print(multiTypeMatrix, len(multiTypeMatrix), type(multiTypeMatrix))
# multiTypeMatrix에서 100이란 값을 출력하기  >> 인덱싱
 # >> 2차원에 속한 값이므로, 차원 축소를 선행한다.
print(multiTypeMatrix[-1])      # 2차원에서 1차원으로 차원축소
print(multiTypeMatrix[-1][-1])  # 축소된 1차원에서 데이터 추출

# 슬라이싱
nums = [1,3,5,7,9]
# nums에서 3,5,7 만 가진 리스트를 추출하기 : 리스트 > 리스트(슬라이싱 : 차원유지)
print(nums[1:-1],'사본 출력')
# 슬라이싱 = 사본 제작 >> 원본은 유지된다. 이 떼, 원본 변경 방법은?
# >> 인덱싱을 활용하여 변경한다
nums[0] = 100
print(nums)
# 3 5 7 을 모두 -1 로 변경하기
# nums[1:-1] = -1     # 변경 불가
nums[1:-1] = '-1'
# 같은 시퀀스(연속데이터)타입이면 슬라이싱을 범위로 대체 가능
print(nums)

# 멤버 삭제
del nums[0]
print(nums)
# 값이 9인 멤버 제거하기
nums.remove(9)
print(nums)
# 중복된 데이터 중 가장 먼저 (정방향)찾은 멤버 제거
nums = [1,3,3,5,5,7,7,9,9,9,11]
nums.remove(3)
print(nums)
# 모두 제거
nums.clear()
print(nums)
# 멤버 추가
nums.append(1)
print(nums)
tmp = [3,5]
# append : 오직 자식 개체로 추가
nums.append( tmp )
print(nums)
# 원본 변경 작업
# extend : 리스트를 이어붙인 것
nums.extend( tmp )
print(nums)
# 사본 작업
print(nums+tmp)     # 리스트 2개를 이어 붙여서 리턴하는 것
print(nums)
# 리스트와 for >> for문에서 확인 예정