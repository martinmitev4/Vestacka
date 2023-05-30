from constraint import *


def raspored(m, p, t):
    if m==1 and p == 0 and t in [14]:
        return True
    if m==0 and p == 1 and t in [13, 16, 19]:
        return True
    ...

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(InSetConstraint([1]), ("Simona_prisustvo",))
    problem.addConstraint(SomeInSetConstraint([1]), ("Marija_prisustvo", "Petar_prisustvo"))

    problem.addConstraint(lambda s, t: (s == 1 and t in [13, 14, 16, 19]), ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(raspored, ("Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    # problem.addConstraint(lambda m, t: (m == 1 and t in [14, 15, 18]), ("Marija_prisustvo", "vreme_sostanok"))
    # problem.addConstraint(lambda p, t: (p == 1 and t in [12, 13, 16, 17, 18, 19]), ("Petar_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------


    nov = dict()
    relust = problem.getSolutions()
    for solution in relust:
        nov["Simona_prisustvo"] = solution["Simona_prisustvo"]
        nov["Marija_prisustvo"] = solution["Marija_prisustvo"]
        nov["Petar_prisustvo"] = solution["Petar_prisustvo"]
        nov["vreme_sostanok"] = solution["vreme_sostanok"]
        print(nov)

# [print(solution) for solution in problem.getSolutions()]
