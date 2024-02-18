# сделать лямбда функцию на квадратное уравнение
from math import sqrt

quadro = lambda x: [(-x[1] - sqrt(discr(x))) / (2 * x[0]), (-x[1] + sqrt(discr(x))) / (2 * x[0])] if discr(x) != "No Solutions" else "No Solutions"
discr = lambda x: (x[1] ** 2) - (4 * x[0] * x[2]) if (x[1] ** 2) - (4 * x[0] * x[2]) >= 0 else "No Solutions"

# ax^2 + bx + c, D = b^2 - 4ac
# x - array[3]

print(quadro([1, -2, -3]))