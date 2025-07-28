import pandas as pd

class Geting_Data:

    @staticmethod
    def return_data(data_path: str, uniq: str) -> dict:
        data = pd.read_csv(data_path)
        count_value = data[uniq].value_counts().to_dict()

        my_dict = {}
        columns = [col for col in data.columns if col != uniq]

        for value in count_value:
            my_dict[value] = {}
            condition = data[data[uniq] == value]

            for col in columns:
                value_counts = condition[col].value_counts().to_dict()
                my_dict[value][col] = {
                    val: value_counts.get(val, 0) + 1
                    for val in data[col].unique()
                }

        return my_dict

    @staticmethod
    def get_data(data_path: str) -> pd.DataFrame:
        return pd.read_csv(data_path)
