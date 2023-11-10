# A deep understanding of multi-process architecture and the threading limitations of Python.

import time
import threading
import multiprocessing

# -------- Multithreading 
# import time
import threading
import numpy as np

# def cal_square(arr):
#     for s in arr:
#         time.sleep(0.2)
#         print('cal_square : ', s*s)

# def cal_cube(arr):
#     for c in arr:
#         time.sleep(0.2)
#         print('cal_cube : ', c*c*c)

# arr = [2,3,8,9]
# t = time.time()

# t1 =  threading.Thread(target=cal_square, args=(arr,))
# t2 =  threading.Thread(target=cal_cube, args=(arr,))

# t1.start()  
# t2.start() 

# t1.join()  
# t2.join() 

# print('done : ', time.time() - t)

# -------- Multiprocessing  
# done :  0.8168680667877197
# done :  1.0650012493133545
square_list = []
def cal_square(arr,result,v):
    # global square_list
    # for s in arr:
    #     print('cal_square : ', s*s)
    #     square_list.append(s*s)
    v.value = 8.9
    print('simple v within : ',v.value )
    for idx,s in enumerate(arr):
        print('cal_square : ', s*s)
        result[idx] = s*s
    print('square_list within', result[:])
if __name__ == '__main__':
    arr = [2,3,8,9]
    result = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',1.2)
    t = time.time()
    t1 =multiprocessing.Process(target=cal_square, args=(arr,result,v))

    t1.start()  
    t1.join()  

    print('square_list OUTSIDE', result[:])
    print('simple v outside : ',v.value )
    print('done : ', time.time() - t)

