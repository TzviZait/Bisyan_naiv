from geting_data import Geting_Data
from classifier import Classifier
from precent import Precent


class Meneger:

    @staticmethod
    def print_meneger():
        run = 1
        while run:
            chois = input("What do you want to do?\n"
                "1.to sey classifier\n"
                "2.to sey precent\n"
                "3.to exit"
                "enter your chois: ")
            if chois == "1":
                data = Geting_Data.get_data()
                uniq = Geting_Data.get_uniq()
                sort_data = Geting_Data.return_data(data, uniq)
                spci_data = Classifier.data_classifier()
                d = Classifier.return_calculete(sort_data, spci_data)
                print(d)
                print(Classifier.print_result(d))

            if chois == "2":
                data = Geting_Data.get_data()
                uniq = Geting_Data.get_uniq()
                a = Precent.result_prcent(data,uniq)
                print(a)

            if chois == "3":
                run = 0

Meneger.print_meneger()

