
def num_to_name(id):
    f = open("file.txt", 'r')
    name = "empty"
    lines = f.readlines()
    for line in lines[1:]:
        tokens = line.split(",")
        if tokens[0] == str(id):
            name = tokens[1]
            print(f"{tokens[1]}: {tokens[0]}")

    if name == "empty":
        print("No Name")
    f.close()
    return name
# name = num_to_name(133)

def name_to_num(name):
    f = open("file.txt", 'r')
    name_x = "empty"
    lines = f.readlines()
    for line in lines[1:]:
        tokens = line.split(",")
        if tokens[1] == name:
            name_x = tokens[1]
            print(f"{tokens[1]}: {tokens[0]}")

    if name_x == "empty":
        print("No Name")
    f.close()
    return name

name_to_num("Ayşe Demir")
