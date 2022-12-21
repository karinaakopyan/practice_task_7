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
