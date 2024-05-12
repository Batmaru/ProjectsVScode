# Marwan Rafik
# 17/04/2024


print("hello world!")

#2.3

#versione breve
name: str = "Mario"
print(f"Ciao {name}")

#versione lunga chomprension
message: str = f"ciao {name}, ti va di imparare un pò di python?"
print(message)

#2.4
#name, name.upper, name.lower
name_upper=name.upper()
name_lower=name.lower()

print(f"{name}, {name_upper}, {name_lower}")

#2.5
phrase: str= "A person who never made a mistake never tried anythingei"
name_p: str= 'Albert Einstein'
print(f'{name_p} una volta disse: "{phrase}"')

#2.8
filename: str= "phyton.txt"
print(filename.removesuffix(".txt"))

#3.1
name: list = ["marwan", "marco", "silvio", "alberto", "antonio"]
for names in name:
    print(f"{names}")   

#3.2
for names in name:
    print(f"ciao, {names}, come stai?")  
    print()