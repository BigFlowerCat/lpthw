# Names Variables Code and Functions

# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, wo can just do this
def print_tow_again(arg1, arg2):
    print(f"arg1: {arg1}k arg2:{arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")


print_two("zed","Shaw")
print_tow_again("Zed", "Shaw")
print_one("First!")
print_none()
