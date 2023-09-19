def f(x):
    return x ** 2

def g(x):
    return x + 1



x = 3

gf = g(f(x))
gg = g(g(x))
ff = f(f(x))
fg = f(g(x))

print(f"(g ° f)({x}) = {gf}")
print(f"(g ° g)({x}) = {gg}")
print(f"(f ° f)({x}) = {ff}")
print(f"(f ° g)({x}) = {fg}")
