import pandas as pd

# xlrd 1.2.0 패키지 설치 필수
def load_searchWord():

    df = pd.read_excel("./data_file/SearchWords.xlsx", sheet_name=0)  # can also name of sheet
    my_list = df['단어/용어'].tolist()

    return my_list