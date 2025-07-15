
class Classifier:

    @staticmethod
    def return_calculete(dic,args):
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
        return my_dict


    @staticmethod
    def print_result(dic):
        a = max(dic, key=dic.get)
        return a
    @staticmethod
    def data_classifier():
         data = input("enter your spsific data:")
         data = data.split(',')
         return data
