import json

import pandas as pd
from numpy.ma.extras import unique


def get_data(data,uniq):
    data = pd.read_csv(data)
    my_dict = {}
    count_value = {}
    for i in data[uniq]:
        if i in count_value:
            count_value[i] += 1
        else:
            count_value[i] = 1

    for i in data[uniq]:
        my_dict[i] = {}

        for c in [col for col in data.columns[1:] if col != uniq ]:
            my_dict[i][c] = {}


            for v in data[c]:
                if v not in my_dict[i][c]:
                    my_dict[i][c][v] = 0


        conthtion = data[data[uniq] == i]


        for j in conthtion.columns[1:]:
            if j != uniq:
                for s in conthtion[j]:
                    if s in my_dict[i][j] :
                        my_dict[i][j][s] += 1

                if 0 in my_dict[i][j].values():
                    my_dict[i][j] = {k: v + 1 for k , v in my_dict[i][j].items()}

    return(my_dict)

def print_calculete(dic,*args):
    s = 0
    c = 1
    my_dict = {}

    for i in dic:
        for j in dic[i]:

            for v in dic[i][j]:
                s += dic[i][j][v]

            for v in dic[i][j]:
                if v in args:
                    c *= dic[i][j][v]/s
            s=0
        my_dict[i] = c
        c = 1
    print(my_dict)

a = get_data("buy_computer_data.csv","age")
print_calculete(a,"senior","low","no","excellent")