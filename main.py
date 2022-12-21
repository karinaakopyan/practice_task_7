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
