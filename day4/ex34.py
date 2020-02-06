# Accessing Elements of Lists


def what_animal(loc):

    animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
    dict ={1:"first", 2:"second", 3:"third", 4:"fourth", 5:"fifth", 6:"sixth"}
    if loc > animals.__len__():
        print("What the h**l are you talking about, man?")
    else:
        order = loc + 1
        order_result = dict[order]
        print(f"The animal at index {loc} is {animals[loc]} and it is at the {order_result} animal.")

what_animal(2)