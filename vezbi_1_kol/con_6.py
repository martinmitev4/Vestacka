import math

from constraint import *


def soberi(s, e, n, d, m, o, r, y):
    # print(s, e, n, d, m, o, r)

    br1 = s * 1000 + e * 100 + n * 10 + d
    br2 = m * 1000 + o * 100 + r * 10 + e
    z = br2 + br1

    c0 = math.trunc(z / 10000)
    c1 = math.trunc((z /1000) % 10)
    c2 = math.trunc((z / 100) % 10)
    c3 = math.trunc((z / 10) % 10)
    c4 = math.trunc(z % 10)

    # print(z)
    # print(c0)
    # print(c1)
    # print(c2)
    # print(c3)
    # print(c4)

    if 0 <= c0 < 10 and 0 <= c1 < 10 and 0 <= c2 < 10 and 0 <= c3 < 10 and 0 <= c4 < 10:
        if c0 == m and c1 == o and c2 == n and c3 == e and c4 == y:
            return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(soberi, ("S", "E", "N", "D", "M", "O", "R", "Y"))

    # ----------------------------------------------------

    print(problem.getSolution())
