import sys

def create():
    the_list = []
    x = r"C:/Users/Admin/practice_it/data_file.csv"
    with open(x,"r") as f:
        reader= f.readlines()
        for row in reader:
            the_list.append(row.strip().split(","))
    return the_list


def create_country():
    country = []
    year = []

    the_list = create()

    for i in the_list:
        if i[6]==sys.argv[4]:
            year.append(i[9])

for i in the_list:
        if i[6] == sys.argv[4] and i[9] == str(sys.argv[5]):
            country.append(i)
    return country
def create_medals ():
    bronze = 0
    silver = 0
    gold = 0
    country = create_country()
    for i in country:
            if i[-1]=="Silver":
                silver +=1
            elif i[-1]=="Gold":
                gold +=1
            elif i[-1]=="Bronze":
                bronze +=1
    return bronze, silver, gold


def medals():
    medal = ""
    counter = 0
    country = create_country()
    BSG = create_medals()
    for i in country:
        if counter == 10:
            break
        if i[-1] == "NA":
            continue
        else:
            print (f"Name: {i[1]}, sport: {i[-2]}, medal: {i[-1]} ")
            counter += 1
            medal+=f"Name: {i[1]}, sport: {i[-2]}, medal: {i[-1]} \n "
    print(f"The number of medals in is: bronze - {BSG[0]}, silver - {BSG[1]}, gold - {BSG[2]} ")
    medal+=f"The number of medals in is: bronze - {BSG[0]}, silver - {BSG[1]}, gold - {BSG[2]} \n "
    return medal


def output ():
    try:
        text = medals()
        a = sys.argv[6]
        with open (sys.argv[7], "a") as f:
            f.write (text)

    except:
        medals()
output()
