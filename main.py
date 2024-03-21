f_string = input("Digite a definição da função f(x) (por exemplo, 'x^2'): ")
g_string = input("Digite a definição da função g(x) (por exemplo, 'x-1'): ")


def f(x):
    return eval(f_string.replace("^", "**"))   

def g(x):
    return eval(g_string.replace("^", "**"))   


def g_f(x):
    return g(f(x))

def g_g(x):
    return g(g(x))

def f_f(x):
    return f(f(x))

def f_g(x):
    return f(g(x))


x = int(input("Digite o valor de x: "))


print(f"(g°f)(x) = {round(g_f(x))}")
print(f"(g°g)(x) = {round(g_g(x))}")
print(f"(f°f)(x) = {round(f_f(x))}")
print(f"(f°g)(x) = {round(f_g(x))}")
