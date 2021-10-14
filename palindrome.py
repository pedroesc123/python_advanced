# def is_palindrome(string: str) -> bool:
#     string = string.replace(" ", "").lower()
#     return string == string[::-1]

# def run():
#     print(is_palindrome(1000))

# if __name__ == "__main__":
#     run()

def es_primo(numero: int) -> str:
    for i in range(2, numero):
        if numero % i == 0:
            alert = "El número no es primo."
            break
        else:
            alert = "El número es primo."

    return alert

def run():
    print(es_primo("ana"))

if __name__ == "__main__":
    run()