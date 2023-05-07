

import random

def functionA():
    print('A')

def a():
    X = random.randint(0,1)
    if X == 1: 
        functionA()
    else:
        functionA()
        print('다시')
        a()

a()




#해당 과정 성공. 턴 이동 알고리즘에서 쓸 수 있을듯

#for문 사용해서 만들 수 있을 것 같음.

#가운데 전환부분 생략한 채로 그냥 숫자느낌으로 1차구현하면 될듯. 알고리즘이 우선임.