import pandas as pd

from classifier import Classifier

from geting_data import Geting_Data

class Precent:

    @staticmethod
    def result_prcent(file_csv,uniq):
        true = 0
        false = 0
        data = pd.read_csv(file_csv).iloc[:500]
        test_data = data.drop(uniq, axis=1)
        count = len(data)
        dic_data = Geting_Data.return_data(data, uniq)

        for index, row in test_data.iterrows():
            a = Classifier.return_calculete(dic_data, row.values.tolist())
            if Classifier.print_result(a) == data[uniq][index]:
                true += 1
            else:
                false += 1

        return true / count * 100

Precent.result_prcent('mushroom.csv', 'class')