import numpy as np
from random import randrange

def think_a_number():
    machine_number = np.array([], np.int8)
    while(len(machine_number) < 4):
        n = randrange(10)
        if(n not in machine_number):
            machine_number = np.append(machine_number, np.array(n))
    return machine_number

def guess_number():
    num = think_a_number()
    
    while True:
        my_num = input('Guess:')
        try:
            if(my_num.isdigit() and len(my_num) == 4):
                if(check_numbers(num, np.array(list(my_num), dtype = int))):
                    break
        except ValueError:
            print('error')
            break
    
def check_numbers(num_arr, my_num_arr):
    cows_correct_value = 0
    bulls_correct_value = 0
    iscorrect = False
    
    for el in my_num_arr:
        if(el in num_arr):
            cows_correct_value = cows_correct_value + 1
            
    if(cows_correct_value != 0):
        for i in range(0, len(num_arr)):
            if(num_arr[i] == my_num_arr[i]):
                bulls_correct_value = bulls_correct_value + 1
    
    if(bulls_correct_value == 4):
        iscorrect = True
            
    '''
    uncomment next code line for show the correct value
    '''
    #print(num_arr)
    print(my_num_arr)
    print('Response: ', bulls_correct_value ,' bulls, ', cows_correct_value - bulls_correct_value , ' cow', )
    return iscorrect

guess_number()