import random

import time


def turn():
    random_list = [random.randint(0, 1) for x in range(4)]


    s = sum(random_list)

    if s == 1:
        if random_list == [1,0,0,0]:
            result = "빽도"
        else:
            result = "도"
    elif s == 2:
        result = "개"
    elif s == 3:
        result = "걸"
    elif s == 4:
        result = "윷"
    else:
        result = "모"

    print ('굴리는중.')
    time.sleep(0.4)
    print('굴리는중..')
    time.sleep(0.4)
    print('굴리는중...')
    time.sleep(0.4)


    print('결과는',result,'!')


turn()