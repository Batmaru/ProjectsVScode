file =  open("file.txt")

with open("file.txt") as file:
    pass

# funzionamento with
class ContextManager:

    def __enter__(self):
        print("Risorsa acquisita")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            pass

        print("Risorsa Rilasciata")
        return False
    
with ContextManager() as manager:
    print("Sono dentro With")