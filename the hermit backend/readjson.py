import json
import os
# paths = [ k for k in os.listdir("CMSU/") if os.path.isfile(os.path.join("CMSU/", k)) ]
# print(paths)
# print('[')
# for j in paths :
#     f = open("CMSU/" + j)
#     MW_raw = json.loads(f.read())
#     Att = [int(i) for i in MW_raw['LowA'][19:47]]
#     for k in Att :
#         if(k > 30115) :
#             continue
#     print(Att , ',')
# f = open("envy.json")
# MW_raw = json.loads(f.read())
# Att = [int(i) for i in MW_raw['LowA'][19:47]]
# print(Att , ',')
f = open('CMSU/01.json')
MW = json.loads(f.read())
for i in MW:
    payload = [k for k in MW[i][19:47]]
    print(i , payload) 

