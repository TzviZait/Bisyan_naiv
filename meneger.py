from geting_data import Geting_Data
from classifier import Classifier

class Meneger:

    @staticmethod
    def print_meneger():
        chois = input("What do you want to do?\n"
              "1.to sey classifier\n"
              "enter your chois: ")
        if chois == "1":
            data = Geting_Data.get_data()
            uniq = Geting_Data.get_uniq()
            sort_data = Geting_Data.return_data(data, uniq)
            spci_data = Classifier.data_classifier()
            d = Classifier.return_calculete(sort_data, spci_data)
            print(d)
            print(Classifier.print_result(d))
Meneger.print_meneger()
