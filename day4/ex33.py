# While loops

i = 0
numbers = []

def while_test(i, numbers, times):
    while i < times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ", numbers)

    for num in numbers:
        print(num)

while_test(i, numbers, 6)