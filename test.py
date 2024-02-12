import re

import json



# json.load関数を使ったjsonファイルの読み込み
with open('custom.json') as f:
    custom = json.load(f)
    
with open('atom.json') as f:
    atoms = json.load(f)
    
atom_dict = {**custom, **atoms}


def calcMW(text):
    if "(" in text:
        level = 0
        isinner=0
        result = ""
        for i in range(len(text)):
            if text[i] == "(":
                level+=1
                if isinner == 0:
                    first = i
                    isinner=1
            elif text[i] == ")":
                level-=1
            if level>0:
                result+=text[i]
            elif isinner==1:
                result+=text[i]
                #print(text[i:])
                m = re.search(r'^[0-9]*',text[i+1:])
                #print(m)

                return calcMW(text[:first] + result[1:-1]*int(m.group(0)) + text[i+1+len(m.group(0)):])
    else:
        parse = re.finditer(r'([A-Z][a-z]?)([0-9.]*)',text)
        iter_parse = list(parse)
        MW = 0
        for i in range(len(iter_parse)):
            try:
                MW += atom_dict[iter_parse[i].group(1)]*float(iter_parse[i].group(2))
            except:
                MW += atom_dict[iter_parse[i].group(1)]
        return MW




# テスト
input_text = "Fe0.95O"
pre = calcMW(input_text)
print(pre)



