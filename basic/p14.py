# 모듈화 * 패키지
# 모듈 만들기, 테스트 코드 배치, 모듈 가져오기, 패키지 사용
    # /basic/a/b/mod.py , /basic/a/__init__.py , /basic/a/b/__init__.py 생성
# 모듈 : *.py 
    # ex : mod.py, __init__.py, p1.py, p2.py
# 모듈화의 대상 : 변수, 함수, class
    # 위의 요소들을 가져와서 자유롭게 사용가능
    # ex : PI, PI2, PI3, add(), XMan
# 패키지 : 유사한 기능끼리 묶어놓은 디렉토리. ex) 유틸리티, 통신, GUI, etc...
    # ex : a, b 폴더
    # 패키지 폴더 내의 __init__.py 파일은 하위 호환을 위해서 python3.3 이하에서는 모두 사용한다
        # 또한, __init__.py 는 해당 패키지 자체를 의미한다

# from : 패키지를 찾아가는 함수.
# from 패키지.패키지.모듈 import 변수,함수,class(필요한 것을 나열한다) 순으로 사용
from a.b.mod import PI, add
print(PI)
print(add)

# from 패키지.패키지 import 변수,함수,class(필요한 것 나열)
# 마지막 경로 상 마지막 패키지(디렉토리)안에 있는 __init__.py 에서 모듈을 가져온다.
from a.b import PI2 as pi2
print(pi2)

# 패키지 명은 . (콤마)가 절대로 사용 불가
# 모듈 명은 . (콤마)가 절대로 사용 불가
from a import PI3
print(PI3)

# 별칭 : 기존의 이름이 너무 길거나, 이름 변경을 해서 사용하고 싶을 때 사용
    # 기존이름 as 별칭
from a import PI3 as pi
print(pi)

# 가져올 모듈의 수가 많지만, 모두 가져오고 싶을 때 : * 사용
# 하위 호환을 위해서
    # __all__=['mod']
from a.b import *
print(mod.PI, PI2)


# import 만 사용하는 방법
import a.b.mod as m
print( m.PI )       # 외장함수 스타일

import a.b as bm
print(bm.PI2)

# 모듈을 가져온다는 것은 해당 모듈을 실행한다는 의미 >> 메모리 적제 필요
# 사용자가 만든 모듈의 경우, 의도하지 않은 코드가 실행될 수 있다
    # 테스트 하려고 만든 코드는 모듈 가져오기 수행시 실제로 구동되면 안된다
    # 이러한 코드는 처리가 필요하다
    # __name_을 이용하여 처리할 것  >> __name__ 이 __main__으로 나온다
    # 모듈로 사용되면(즉, 다른 모듈이 가져와서 사용하면), "모듈명"으로 표현된다

from p13_mod import XMan
mu = XMan('하하', 100, 50, 65)
print( mu )
print('p14 : __name__', __name__)
