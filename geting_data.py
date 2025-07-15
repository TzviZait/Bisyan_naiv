import pandas as pd

class Geting_Data:

    @staticmethod
    def return_data(data,uniq):
        my_dict = {}

        for i in data[uniq]:
            my_dict[i] = {}
            for c in [col for col in data.columns if col != uniq ]:
                my_dict[i][c] = {}
                for v in data[c]:
                    if v not in my_dict[i][c]:
                        my_dict[i][c][v] = 0

            conthtion = data[data[uniq] == i]

            for j in conthtion.columns:
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
        return data

    @staticmethod
    def get_uniq():
        uniq = input("enter the uniq collonm:")
        return uniq

# print(Geting_Data.return_data(Geting_Data.get_data(),"Buy_Computer"))

# import pandas as pd
#
#
# class Geting_Data:
#     @staticmethod
#     def return_data(data, uniq):
#         # שלב 1: ספירת ערכים בעמודה uniq
#         count_value = data[uniq].value_counts().to_dict()
#
#         # שלב 2: בניית מילון עבור כל ערך של uniq
#         my_dict = {}
#         # עמודות ללא uniq בלבד (כולל העמודה הראשונה)
#         columns = [col for col in data.columns if col != uniq]
#
#         # עבור כל ערך ייחודי ב-uniq
#         for value in count_value:
#             my_dict[value] = {}
#             # סינון השורות עבור הערך הנוכחי של uniq
#             condition = data[data[uniq] == value]
#
#             # עבור כל עמודה
#             for col in columns:
#                 # ספירת ערכים בעמודה עבור התנאי
#                 value_counts = condition[col].value_counts().to_dict()
#
#                 # יצירת מילון עם כל הערכים האפשריים (כולל כאלה שלא מופיעים בתנאי)
#                 my_dict[value][col] = {
#                     val: value_counts.get(val, 0) + 1  # Laplace smoothing: הוספת 1
#                     for val in data[col].unique()
#                 }
#
#         return my_dict
#
#     @staticmethod
#     def get_data():
#         data = input("enter your data:")
#         data = pd.read_csv(data)
#         return data
#
#     @staticmethod
#     def get_uniq():
#         uniq = input("enter the uniq collonm:")
#         return uniq