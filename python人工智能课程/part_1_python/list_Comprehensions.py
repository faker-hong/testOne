# Quiz Solution: Extract First Names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_name = [name.split()[0].lower() for name in names]
print(first_name)


# Quiz Solution: Filter Names by Scores
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

names = [name for name, score in scores.items() if score >= 65]
print(names)