import pandas as pd


def load_searchWord():

    df = pd.read_excel("./data_file/SearchWords.xlsx", sheet_name=0)  # can also name of sheet
    my_list = df['단어/용어'].tolist()

    return my_list