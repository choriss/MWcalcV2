import re

def calcMW(text):
    m = re.search(r'\((.*?)\)', text)
    if m is None:
        #カッコなし時の処理

        pass
    else:
        #カッコあり時の処理
        calcMW(m.group(1))
        pass

# 例を試す
text = "これは(Pythonで)作られた(例文)です。"
print(calcMW(text))  # ['Pythonで', '例文']
