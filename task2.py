import pandas as pd

data = [
["L01","EcoBook 13",450,55,10,1.3],
["L02","Titan G9",2800,99,8,2.8],
["L03","Enduro Air",1200,75,20,1.4],
["L04","Feather X",1500,80,12,0.95],
["L05","Flow 198",1267,51,16,1.8],
["L06","Apex 196",1363,55,17,1.78],
["L07","Prime 439",753,46,8,1.82],
["L08","Elite 551",2852,87,4,3.27],
["L09","Zenith 235",599,44,7,1.86],
["L10","Flow 688",1356,65,18,1.52],
["L11","Workmate 817",1396,66,15,1.8],
["L12","Swift 682",3215,75,4,2.98],
["L13","Swift 459",1379,59,16,2.19],
["L14","Flow 924",3155,82,4,3.46],
["L15","Gamer Pro 845",1854,58,8,1.53],
["L16","Gamer Pro 573",2039,73,7,1.64],
["L17","Core 322",1812,66,7,1.27],
["L18","Prime 298",1690,69,9,1.41],
["L19","Inspire 728",1349,69,15,1.83],
["L20","Core 209",2936,80,4,3.43],
]

df = pd.DataFrame(data, columns=["ID","Model","Price","Performance","Battery","Weight"])

pareto = []

for i,row in df.iterrows():
    dominated = False
    
    for j,other in df.iterrows():
        if i != j:
            if (other["Price"] <= row["Price"] and
                other["Performance"] >= row["Performance"] and
                other["Battery"] >= row["Battery"] and
                other["Weight"] <= row["Weight"] and
                (other["Price"] < row["Price"] or
                 other["Performance"] > row["Performance"] or
                 other["Battery"] > row["Battery"] or
                 other["Weight"] < row["Weight"])):
                
                dominated = True
                break
    
    if not dominated:
        pareto.append(row)

pareto_df = pd.DataFrame(pareto)

print("Pareto Optimal Laptops:")
print(pareto_df)
