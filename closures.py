# def make_repeater_of(n):
#     def repeater(string):
#         assert type(string) == str, "Solo puedes utilizar cadenas."
#         return string * n
#     return repeater

# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5("Hola"))
#     repeat_10 = make_repeater_of(10)
#     print(repeat_10("Platzi"))

def make_division_by(n: int):
    def division(x: int) -> int:
        assert n != 0, "No puedes dividir por 0"
        return int(x/n)
    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))

if __name__ == "__main__":
    run()