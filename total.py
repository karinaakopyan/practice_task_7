import sys


def total():
    dict = {}
    file = sys.argv[1]
    year = sys.argv[3]
    with open(file, "r") as f:
        line = f.readline()
        while line:
            lines = line.split("\t")
            medals = lines[-1][:-1]
            years = lines[9]
            countries = lines[7]
            if countries and countries in lines:
                if medals != "NA":
                    if countries not in dict and years == year:
                        dict[countries] = [0, 0, 0]
                    if medals == "Gold" and years == year:
                        dict[countries][0] += 1
                    if medals == "Silver" and years == year:
                        dict[countries][1] += 1
                    if medals == "Bronze" and years == year:
                        dict[countries][2] += 1

            line = f.readline()
        for countries, medals in dict.items():
            if medals != [0, 0, 0]:
                print(f"{countries} - {medals[0]}, {medals[1]}, {medals[2]} ")


total()
