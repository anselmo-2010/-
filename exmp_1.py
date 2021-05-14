passw = input("Введите пароль")

def test_passw(p):
    def deco(f):
        if p == "10":
            return f
        else:
            return lambda: "Доступ закрыт"
    return deco


@test_passw(passw)
def func():
    return "Доступ открыт"
print(func())