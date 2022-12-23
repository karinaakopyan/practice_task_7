import sys


def create():
    lst = []
    x = r"data_file.csv"
    with open(x, "r") as f:
        lines = f.readlines()
        for row in lines:
            lst.append(row.strip().split(","))

    return lst

def countries():
        country = []
        year = []
        for i in create():
            if i[6] == country_name or i[7]==country_name:
                year.append(i[9])

        for i in create():
            if i[6] == country_name or i[7]==country_name:
                country.append(i)
        year=sorted(list(set(year)))

        return country,year


def first_place():
    x=countries()
    country=x[0]
    year=x[1][0]
    info=None
    for i in country:
        if i[9]==year:
            info=[year,i[-4]]
            break
    return info

def medals(year):
    bronze = 0
    silver = 0
    gold = 0

    for i in countries()[0]:
        if i[9]==year:
            if i[-1] == "Silver":
                silver += 1
            elif i[-1] == "Gold":
                gold += 1
            elif i[-1] == "Bronze":
                bronze += 1
    return bronze, silver, gold,bronze+silver+gold

def total_medals():
    x=countries()
    year=x[1]
    medal=[]
    for i in year:
        medal.append([i,medals(i)])
    return medal

def min_max_average():
    medal=total_medals()
    medal_list=[i[-1][-1] for i in medal]
    min_=min(medal_list)
    max_=max(medal_list)
    min_list=[]
    max_list=[]

    for i in medal:
        if i[-1][-1]==min_:
            min_list.append([i[0],i[-1][-1]])
        elif i[-1][-1]==max_:
            max_list.append([i[0],i[-1][-1]])

    silver_list=[]
    gold_list=[]
    bronze_list=[]

    for i in medal:
        bronze_list.append(i[-1][0])
        silver_list.append(i[-1][1])
        gold_list.append(i[1][2])

    av_silver = sum(silver_list)/len(medal)
    av_gold = sum(gold_list)/len(medal)
    av_bronze = sum(bronze_list)/len(medal)


    return min_list,max_list,[av_bronze,av_silver,av_gold]


def interactive():
    global country_name
    country_name = input("Enter country name or country code")

    first=first_place()
    mma=min_max_average()
    print(f"First olympics:\n",first[0],first[1])

    print(f"\nMax:")
    for i in mma[1]:
       print(i[0],i[1])
    print(f"\nMin:")
    for i in mma[0]:
       print(i[0],i[1])
    print(f"\nAvarage: bronze {mma[2][0]}, silver {mma[2][1]}, gold {mma[2][2]}")
interactive()