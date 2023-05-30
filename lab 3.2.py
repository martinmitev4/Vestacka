from constraint import *

def nekoja(*args):

    ...


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    ...

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    variables = ("AI", "ML", "NLP")
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(AllDifferentConstraint(), variables)

    problem.addConstraint(nekoja, ())

    result = problem.getSolution()

    # print(result)

    # Tuka dodadete go kodot za pechatenje

    for key, value in papers.items():
        print(f"{key} ({value}): {result[value]}")

