from constraint import *

# nov = dict()
#
#     for solution in prb:
#         nov["Simona_prisustvo"] = solution["Simona_prisustvo"]
#         nov["Marija_prisustvo"] = solution["Marija_prisustvo"]
#         nov["Petar_prisustvo"] = solution["Petar_prisustvo"]
#         nov["vreme_sostanok"] = solution["vreme_sostanok"]
#         print(nov)


def raspored(marija, petar, t):
    if marija == 1 and petar == 0 and t in [14]:
        return True
    if marija == 0 and petar == 1 and t in [13, 16, 19]:
        return True
    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(InSetConstraint([1]), ("Simona_prisustvo",))

    problem.addConstraint(SomeInSetConstraint([1]), ("Marija_prisustvo", "Petar_prisustvo"))

    problem.addConstraint(raspored, ("Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    problem.addConstraint(InSetConstraint([13, 14, 16, 19]), ("vreme_sostanok",))

    [print(solution) for solution in problem.getSolutions()]
