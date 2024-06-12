# reader = open('esempiofile.txt')
# print(reader)

# try:
#     reader.readline()
#     print("sono nella try")
#     raise Exception('Eccezione')

# except Exception:
#     print("sono nell'except")

# finally:
#     print(reader)
#     reader.close()
#     print("sono nel finally")




# with open("esempiofile.txt") as reader:
#     reader.readline()

# class ContextManager:

#     def __enter__(self):
#         print("Ciao sono nell'enter")
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is not None:

#             print("Eccezione")
#         return False
    
# with ContextManager() as manager:
#     print("Sono dentro With")


# try:
#     with ContextManager() as cm:

#         print('ciao')
#         print(cm)

# except Exception:
#     print()



#metodo per leggere un file

# with open("esempiofile.txt") as reader:
#     # tipi di read:
#     # read() -> legge tutto il file
#     # print(reader.read())
#     # readline() -> legge una riga alla volta
#     # print(reader.readlines())
#     # readlines() -> legge tutte le righe e le restituisce in una lista
#     # print(reader.readline(5))
    
#     line= reader.readline()
#     line_counter=0
#     while line != '':
#         print(f'{line}, number: {line_counter}')
#         line = reader.readline()
#         line_counter+=1

 
# metodo per scrivere una linea
with open("esempiofile.txt", 'a') as reader:
    
    reader.write(f'Ciao sono marwan\n')
    l=[f"ciao sono flavio\n", f"ciao sono marwan\n"]
    reader.writelines(l)