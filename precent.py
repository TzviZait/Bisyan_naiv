import pandas as pd

from classifier import Classifier

from train_bisean_naiv import Geting_Data

class Precent:

    @staticmethod
    def result_prcent(file_csv,uniq):
        true = 0
        data = file_csv
        test_data = data.drop(uniq, axis=1)
        count = len(data)
        dic_data = Geting_Data.return_data(data, uniq)

        for index, row in test_data.iterrows():
            a = Classifier.return_calculete(dic_data, row.values.tolist())
            if Classifier.print_result(a) == data[uniq][index]:
                true += 1
        return true / count * 100

