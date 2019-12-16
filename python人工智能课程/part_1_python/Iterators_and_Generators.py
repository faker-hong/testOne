# Quiz Solution: Implement my_enumerate
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    count = start
    for lesson in iterable:
        yield count, lesson
        count += 1


for i, lesson in my_enumerate(lessons, start=1):
    print(i, lesson)



# Quiz Solution: Chunker
def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]


for chuk in chunker(range(30), 6):
    print(list(chuk))