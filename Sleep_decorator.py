#Sleep decorator
#gdy np dana funkcja musi się odświeżyć co jakiś określony czas

import functools
import time

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
    
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Koniec!")
    else:
        print(from_number)
        countdown(from_number-1)
        
countdown(10)
