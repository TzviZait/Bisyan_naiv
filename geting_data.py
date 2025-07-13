import pandas as pd

class Geting_Data:

    @staticmethod
    def return_data(data,uniq):
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

        return my_dict

    @staticmethod
    def get_data():
        data = input("enter your data:")
        data = pd.read_csv(data)
        return data.iloc[:, 1:]

    @staticmethod
    def get_uniq():
        uniq = input("enter the uniq collonm:")
        return uniq


