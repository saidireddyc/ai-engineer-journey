name = input("Enter your name: ")

if name == "":
    print("You didn't enter a name")
else:
    print("Hello", name)

def greet(person):
    return "Welcome " + person

print(greet(name))