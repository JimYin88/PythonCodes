'''
Created on Jun 10, 2022

@author: Jim Yin
'''

from multiprocessing import Process, Manager
import time
import math

def make_calculation_one(numbers, return_dict):
    results_a = []
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))
    
    print(sum(results_a))
    return_dict['one'] = sum(results_a)
    return (sum(results_a))
        
        
def make_calculation_two(numbers, return_dict):
    results_b = []
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))
        
    print(sum(results_b))
    return_dict['two'] = sum(results_b)
    return (sum(results_b))
        
        
def make_calculation_three(numbers, return_dict):
    results_c = []
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))
        
    print(sum(results_c))
    return_dict['three'] = sum(results_c)
    return (sum(results_c))
        
        
if __name__ == '__main__':
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    number_list = list(range(5000000))
    
    start_time = time.perf_counter()
    
    process1 = Process(target=make_calculation_one, args=(number_list, return_dict))
    process1.start()
    processes.append(process1)
    process2 = Process(target=make_calculation_two, args=(number_list, return_dict))
    process2.start()
    processes.append(process2)
    process3 = Process(target=make_calculation_three, args=(number_list, return_dict))
    process3.start()
    processes.append(process3)
    
    # print(Q.get())
    # result = []
    # for i in range(3):
    #     val = Q.get(block=True) # wait for the next item
    #     result.append(val)
    
    for p in processes:
        p.join() # wait for finish of jobs
        
    print(return_dict.values())
    
    final_result = return_dict.values()
    
    for a in final_result:
        print(a)
    # totalworkdone = tuple(result)
    # print(totalworkdone)


    
    #
    #
    #
    # for proc in processes:
    #     proc.join()
    #
    #

    # process.join()
    # print(results_c[0:20])
    

    
    # start_time = time.perf_counter()
    # print(make_calculation_one(number_list))
    # print(make_calculation_two(number_list))
    # print(make_calculation_three(number_list)
    end_time = time.perf_counter()
    # print(results_c[0:20])
    
    print(f'Time taken = {end_time - start_time} sec')
    
    
    # Time taken = 9.487345300000001 sec

    
    
        
        
    