# 파일 처리, 파일 덤프

# 내장함수
# open()
'''
mode :
    w : 쓰기 모드.
    i : 읽기 모드.
    a : 추가 모드.
    b : 바이너리 모드로 파일 열기.
    + : 반대 속성 추가, r+ == rw
'''
f = open('f1.txt', 'w')
for n in range(10) :
    f.write('%d 라인 line 12!@\n' % n)
f.close()

f = open('f1.txt', 'r')
print(f.read())
f.close()

# 파일을 열어둔 상태로 진행하면 추후 오류 발생
# I/O에서 파일 open 시, 필수적으로 파일을 닫아야 한다.
    # 간혹, 누락시키는 경우 있으므로, 원천적으로 해결하는 것이 좋다
        # 자동으로 닫히도록 설정
# with 문 ~ :  사용     >> close()가 필요없다
with open('f1.txt', 'r') as f :
    print(f.read)


# 외장함수
# pickle : 자료구조를 유지하고, dump하여 load
    # 머신러닝에서도 피클을 커스터마이징해서 지원한다
import pickle as p
data = {
    1:[1,2,3,4],
    2:{'name':'수호랑'},
    3:(5,6,7,8)
}
# dump
with open('data.p','wb') as f1 :    # 쓰기모드를 바이너리로 진행
    p.dump( data, f1, p.HIGHEST_PROTOCOL )
# load
with open('data.p','rb') as f2 :
    tmp = p.load(f2)
    print(tmp, type(tmp))

# OS module
import os
# os.getcwd() : 현재 프로젝트 경로 확인
print(os.getcwd())
# os.listdir(os.getcwd()) : 제시된 디렉토리에 존재하는 모든 파일과 디렉토리를 리스트로 나열
print(os.listdir(os.getcwd()))

