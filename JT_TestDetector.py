import pandas as pd
import win32com.client as win32
import os

# 한글파일을 TEXT파일로 저장하여 한글만 추출
pathlist = "D:/Source_code/Loanword-detector/data_hwp/test1.hwp"

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "AutomationModule")
hwp.Open(pathlist, "HWP", "forceopen:true")
hwp.SaveAs("D:/Source_code/Loanword-detector/data_hwp/" + "tt" + ".txt", "TEXT")
hwp.Quit()


"""
# 엑셀 파일 열 불러오는 함수 *xlrd 1.2.0 패키지 설치 필수
def load_searchWord():

    df = pd.read_excel("./data_file/SearchWords.xlsx", sheet_name=0)  # can also name of sheet
    my_list = df['단어/용어'].tolist()

    return my_list


# 텍스트 파일 불러오기
f = open("./data_file/testFile.txt", mode='r', encoding='UTF8')
text = f.read()
print(text)


print(load_searchWord())

for i in load_searchWord():
    cntNum = text.count(i)
    if cntNum > 0:
        print(i + " : " + str(cntNum))
"""