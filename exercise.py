
import module as md

print("Task 1:")
names = ["Mayowa", "chizoba", "Chigozie"]
print(names[0].split(sep= ("a" or "o")))
print(md.task_one("Tade Gold Wealth") +"\n")

print("Task 2:")
task2 = ["first name", "last_name", "date of birth"]
print(md.task_two(task2))
print("\n")

print("Task 3:")
print(md.last_letter_check(names[1]))
print(md.task_three(names))
print("\n")

print("Task 4:")
entry = ["Wofai", "Na(me", "Zainab", "A4atullah", "Women42k", "Norm1al"]
print(md.task_four(entry))

"""for i in data:
    for j in i:
        if not j.isalpha():
            bad_data.append(i)
print(f"Bad inputs in entry: {bad_data}")"""

"""
names[2] = names[2].replace(names[2][-1], "a") 
print(names[2])

if names[0][0].isupper():
    print(names[0])
else:
    print("Not uppper")


if names[0][0].isupper() and not names[0][-1].endswith("a"):
    print("Yes!")
else:
    print("No!")
"""