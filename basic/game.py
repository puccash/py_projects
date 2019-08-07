# 절차적 프로그래밍 >> 사용자 정의 함수를 사용하지 말 것.
# step 1-1 :
game_txt = [ '게임 제목을 입력하세요\n',
    '아무것도 입력되지 않았습니다. 다시 진행하세요\n',
    '입력하신 "%s"게임 제목은 최대 20자를 초과할 수 없습니다. 다시 입력하세요\n',
    'v1.0.0\n',
    '게이머의 이름을 입력하세요?\n',
    '이름이 입력되지 않았습니다. 다시~\n',
    '다시 게임을 할까요?(yes/no) 대소문자 관계 없이 입력\n',
    '정확하게 (yes/no)로 입력하세요\n',
    'game over !! bye bye~\n'
 ]
game_txtEx = { 'GAME_INTRO':'0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요',
    'INPUT_EMPTY':'값을 정확하게 입력하세요',
    'INPUT_NOT_NUM':'숫자가 아닙니다',
    'out_of_bound':'값이 범위를 넘었습니다. 0~99 사이로 다시 입력하세요',
    'check_err01':'값이 크다', 
    'check_err02':'값이 작다',
    'check_success':'''
    정답입니다. 게이머:{0}, AI:{1}
           {name}님의 총 시도 횟수는 {cnt}회 입니다.
           획득 점수는 {score}점 입니다.
    '''
 }
# cnt : 딕셔너리 구조를 사용하기 위함.
# 게임이 시작하면 다음의 프럼프트가 나온다 : "게임 제목을 입력하시오"
# game_title = input(game_txt[0])
# print('[%s]'%gmae_title)

while True :
    game_title = input(game_txt[0])
    # 값 check
    # 아무것도 입력하지 않으면 => 아무것도 입력하지 않았습니다. 다시!!\n
    if not game_title :
        # game_title이 ''이면, 조건문에 도달했을때, false로 판단한다
        # ''은 곧 아무것도 입력하지 않을때를 의미한다.
        print(game_txt[1])
        #pass
    # 20자 초과 입력 시 => 입력하신 "xx" 게임 제목은 최대 20자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요..\n
    elif len(game_title) > 20 : 
        print(game_txt[2] % ( game_title, len(game_title) ))
        #pass
    # 정상입력
    else :
        #print('[%s]'%gmae_title)
        # 정상입력 시, 해당 반복문에서 빠져 나온다.
        #pass
        break
print('[%s]' % game_title)        
# step 1-2 :
# 게임 프럼프트 출력 (가로 26칸), 한글 제목일 경우 간격이 안 맞는 부분은 우선 배제한다
cell_amt = 26
# 포멧팅 사용하는 기호가 서로 다르므로, 다른 케이스로 글자크기를 조절한다.
# 아래의 form 에서 글자 수를 2개 빼는 이유 : 틀 형식인 = 2개 뺀 것
form = '={0:^%s}=' % (cell_amt-2)
#==============================
print('='*cell_amt)
#=          게임제목           =
#print('={0:^24}='.format(game_title))
print(form.format(game_title))
#=           v1.0.0           =
#print('={0:^24}='.format(game_txt[3]))
print(form.format(game_txt[3]))
#==============================
print('='*cell_amt)
# 26 이란 수치를 40으로 변경되어도 잘 적응되게 코드 보정

    #print('='*30)
    #print('{0:<10}'.format('='), '{0:^4}'.format('게임제목'), '{0:>10}'.format('='))
    #print('{0:<10}'.format('='), '{0:^8}'.format('v1.0.0'), '{0:>10}'.format('='))
    #print('='*30)

# step 2 : 
# 게이머의 이름을 입력하세요?
# 입력되지 않으면 => 이름이 입력되지 않았습니다. 다시~'
# flag 변수 : 상황을 통제하고 구분하는 변수.
nameCheck = True   # 1 
while nameCheck :   # 2
    gamer_name = input(game_txt[4]) # 3
    #print(gamer_name)
    if not gamer_name  :    # 3-1  >> 3 으로 이동
        print(game_txt[5])
    # else :
        #print('정상입력', gamer_name)
        # 다시 조건을 check하고, 코드를 더이상 진행하지 않을 때
        continue    # 4
    # 이름을 정상입력하면 > 반복문 종료 시점
    nameCheck = False   # 5
print('정상입력', gamer_name)
# 진행 순서 : 1 > 2 > 3 (입력 X 인 경우) > 3-1 > 3 (입력된 경우) > 4 > 5 > 종료

# step 3 ~ 5 동일 반복 구간
# ai_num 값이 없음 - step 4 참조, step 5 기본 구성후 추가.
game_run = True     # flag 함수. 
while game_run :
    # 게임 변수 초기화 Start ===
    ai_num = None
    # 시도 횟수 부여 (추가)
    try_count = 0
    # 게임 변수 초기화 End ===
    while True :
        # step 3 : 
            # 게임 방식 간단히 설명하고, => ''' 본 게임음 ... '''
        # 본게임 시작
        # "0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요" 출력하고 다시 입력 대기
        while True :
            gamer_num = input(game_txtEx['GAME_INTRO']).strip() # strip을 사용해 공백을 제거한다

            # '값을 정확하기 입력하세요' 출력하고 다시 입력 대기
            # '숫자가 아닙니다' 출력하고 다시 대기 입력
            # '값이 범위를 넘어었습니다. 0~99 사이로 다시 입력' 출력하고, 다시 입력 대기 
                # if문 내에서 elif를 쓰지 않고 따로 if문을 재구성하면, 구성을 자유롭게 할 수 있는 특성이 생긴다
            # 문자열의 관점
            if not gamer_num : 
                print(game_txtEx['INPUT_EMPTY'])
                continue    # 하단의 다른 if문에 영향을 주지 않고 현재의 if문에서 사용하는 조건이 종료된다
            elif not gamer_num.isnumeric() :  
            # else 대신 elif를 사용해도 무관하다
            # False인 값은 정수값이 될 수 없다 = 정수가 아니다   
                print(game_txtEx['INPUT_NOT_NUM'])
                continue
            # 문자열의 정수화가 필요하다
            gamer_num = int(gamer_num)
            if gamer_num < 0 or gamer_num > 99 :    # sort 연산방법
                print(game_txtEx['out_of_bound'])
                continue
            # 범위 내의 정수값을 정확하게 획득, 반복문 종료
            break

        # step 4 : 
        # AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99 사이로 1회만 셋팅되도록 고정 필요
        import random
        # ai_num이 값이 없었을때, 초기화 한다 (None 부여)
        if not ai_num :
            ai_num = random.randint(0,99)
            print( 'ai_num', ai_num )

        try_count +=1
        # step 5 : 
        # AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다 => 맞출때까지 반복
            # gamer_num , ai_num 사용하기
        if gamer_num > ai_num :
            print(game_txtEx['check_err01'])
        elif gamer_num < ai_num :
            print(game_txtEx['check_err02'])
        else :  # 정답
            print(game_txtEx['check_success'].format(
                gamer_num,
                ai_num,
                score=(100-try_count*10) ,
                cnt=try_count ,
                name= gamer_name
            ))
            #정답이면 
            #정답입니다. 게이머:{0}, AI:{1}
            #    {name}님의 총 시도 횟수는 {cnt}회 입니다.
            #    획득 점수는 {score}점 입니다.
            # 점수 : 100-시도횟수*10
            break

    # step6 :
    # 다시 게임을 할까요?(yes/no) 대소문자 관계 없이 입력
    # '정확하게 (yes/no)로 입력하세요'
    # no => 'game over !! bye bye~'
    # yes => 본게임 시작 으로 이동하여 진행
    while True :
        ans = input(game_txt[6]).strip().upper()
        if ans == 'YES' :
            break
        elif ans == 'NO' :
            print(game_txt[8])
            # 전체 게임 종료 지점
            game_run = False
            break
        else :  # 공백, 다른 문자 등 입력 시, 잘못된 입력 전체 의미
            print(game_txt[7])

import sys
# 프로그램 종료
sys.exit