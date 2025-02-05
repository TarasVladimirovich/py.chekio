students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Mathew': 21,
    'Betty': 20
}

print(max(students, key=students.get), min(students, key=students.get))


def rabbit_hole(year):
    rabbits = {"pair_0":0}
    for i in range(year):
        new_born = 0
        for k, v in rabbits.items():
            rabbits[k] += 1
            if rabbits[k] >= 3:
                new_born += 1
        for i in range(new_born):
            rabbits[f"pair_{len(rabbits)}"] = 0
    return rabbits

print(rabbit_hole(5))

