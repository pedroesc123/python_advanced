from datetime import date, datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a:int, b:int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Cesar"):
    print("Hola "+ nombre)

random_func()
suma(5, 5)
saludo("Facundo")


# def upper_first_letter(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs).title()
#     return wrapper

# @upper_first_letter
# def function(message):
#     return message

# print(function("hola como estan"))


