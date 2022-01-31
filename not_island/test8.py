students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Mathew': 21,
    'Betty': 20
}

print(max(students, key=students.get), min(students, key=students.get))
