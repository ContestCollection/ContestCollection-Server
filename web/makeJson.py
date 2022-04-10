import json
from collections import OrderedDict
from DB import getFromDB

datas = getFromDB()

# IT_YEAR_team 팀 나누는 파트
IT_2021_team = OrderedDict()
IT_2020_team = OrderedDict()

# con_year_IT 파트
con_year_IT = OrderedDict()
con_year_IT[2021] = IT_2021_team
con_year_IT[2020] = IT_2020_team

# SW_YEAR_team 팀 나누는 파트
SW_2021_team = OrderedDict()
SW_2020_team = OrderedDict()

# con_year_SW 파트
con_year_SW = OrderedDict()
con_year_SW[2021] = SW_2021_team
con_year_SW[2020] = SW_2020_team

# MC_YEAR_team 팀 나누는 파트
MC_2021_team = OrderedDict()
MC_2020_team = OrderedDict()

# con_year_MC 파트
con_year_MC = OrderedDict()
con_year_MC[2021] = MC_2021_team
con_year_MC[2020] = MC_2020_team

# con_department 파트
con_department = OrderedDict()
con_department["IT"] = con_year_IT
con_department["SW"] = con_year_SW
con_department["MC"] = con_year_MC


# contestData 파트
id = 0
for data in datas:
    contestData = OrderedDict()
    contestData["id"] = id
    id += 1
    contestData["name"] = data[4]
    contestData["award"] = data[5]
    contestData["subTitle"] = data[6]
    contestData["summary"] = data[7]
    contestData["category"] = [data[1]]
    contestData["img"] = data[8]

    contestData["people"] = []
    for i in range(9,13):
        print(data[i])
        if data[i] != None:
            contestData["people"].append(data[i])

    contestData["calendar"] = []
    x = data[13].split(",")
    for y in x:
        z = y.strip()
        contestData["calendar"].append(z)

    contestData["githubLink"] = data[14]
    contestData["youtubuLink"] = data[15]
    contestData["serviceLink"] = data[16]
    contestData["skills"] = data[17]


    globals()[str(data[1]) + "_" + str(data[2]) + "_team"][data[3]] = contestData

# Print JSON
with open('test.json', 'w', encoding="utf-8") as make_file:
    json.dump(con_department, make_file, ensure_ascii=False, indent="\t")