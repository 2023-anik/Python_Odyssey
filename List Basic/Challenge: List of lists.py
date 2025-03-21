def enrollment_stats(universities):
    students = []
    tuitions = []
    for university in universities:
        students.append(university[1])
        tuitions.append(university[2])
    return (students, tuitions)


def mean(data):
    return sum(data) / len(data)

def median(data):
    data.sort()
    if len(data) % 2 == 1:
        return data[len(data)//2]
    else:
        return mean([data[(len(data)-1)//2], data[(len(data)+1)//2]])

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]

totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:    ${sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:     ${mean(totals[1]):,.2f}")
print(f"Tuition median:   ${median(totals[1]):,}")
print("*****" * 6)
print("\n")
