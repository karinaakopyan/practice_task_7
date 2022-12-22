import sys


def create():
    lst = []
    x = r"C:\Users\Cubbi\PycharmProjects\random new project\data-file.csv"
    with open(x, "r") as f:
        lines = f.readlines()
        for row in lines:
            lst.append(row.strip().split(","))
    return lst


def countries():
    country = []
    year = []

    for i in create():
        if i[6] == sys.argv[4]:
            year.append(i[9])

    for i in create():
        if i[6] == sys.argv[4] and i[9] == str(sys.argv[5]):
            country.append(i)
    return country


def medals():
    bronze = 0
    silver = 0
    gold = 0

    for i in countries():
        if i[14] == "Silver":
            silver += 1
        elif i[14] == "Gold":
            gold += 1
        elif i[14] == "Bronze":
            bronze += 1
    return bronze, silver, gold


def medales():
    medal = ""
    counter = 0
    BSG = medals()
    for i in countries():
        if counter == 10:
            break
        if i[-1] == "NA":
            continue
        else:
            print(f"Name: {i[1]}, sport: {i[-2]}, medal: {i[14]} ")
            counter += 1
            medal += f"Name: {i[1]}, sport: {i[-2]}, medal: {i[14]} \n "
    print(f"The number of medals in is: bronze - {BSG[0]}, silver - {BSG[1]}, gold - {BSG[2]} ")
    medal += f"The number of medals in is: bronze - {BSG[0]}, silver - {BSG[1]}, gold - {BSG[2]} \n "
    return medal


def output():
    text = medales()
    a = sys.argv[6]
    with open(sys.argv[7], "a") as f:
        f.write(text)

    medals()
output()


