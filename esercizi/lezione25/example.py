from multiprocessing import Process
import time

def bubble_sort_v2():

    from random import randint
    
    x = [randint(0, 10000) for _ in range(50000)]
    
    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break


# from multiprocessing import Process
# import time

# def sleep():
    
#     print(f"Sono nella funzione")
#     time.sleep(60)
#     print(f"Sto uscendo dalla funzione")
    
# if __name__ == "__main__":
    
#     tic: float = time.time()
#     t1 = Process(target=sleep)
#     t2 = Process(target=sleep)
#     t1.start()
#     t2.start()
#     # t1.join()
#     # t2.join()
#     toc: float = time.time()
#     time_elapsed: float = toc - tic 

#     print(f"{time_elapsed=}")
    
# def parent():
    
#     def figlio_1():
        
#         print(f"Sono in figlio_1")
        
#     def figlio_2():
        
#         print(f"Sono in figlio_2")
        
#     return figlio_1

# func = parent()

# func()
# import time

# def decorator(func):
    
#     def wrapper(*args, **kwargs):
        
#         tic = time.time()
        
#         func(*args, **kwargs)
        
#         print(f"{time.time() - tic}")
        
#     return wrapper

# @decorator
# def esempio(name: str):
    
#     print(f"Ciao, {name}")
       
# @decorator
# def esempio_2(name: str, p2: str):
    
#     print(f"Ciao, {name}")

# esempio(name="Flavio")

# condizione: bool = True and False

# assert 10 > 5, f"Il valore di condizione è {condizione}"

# if 10 > 5:
#     raise ArithmeticError(f"The if condition i wrong!")

# try:
    
#     pass

# except ZeroDivisionError as E:
    
#     pass

# else:
    
#     pass

# finally:
    
#     pass