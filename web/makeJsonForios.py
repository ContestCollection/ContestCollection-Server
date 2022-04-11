import json
from collections import OrderedDict
from DB import getFromDB, getFromDB2

def makejson(part, year, id):
    if part or year or id:
        datas = getFromDB2(part, year, id)
    else:
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
    SW_2019_team = OrderedDict()

    # con_year_SW 파트
    con_year_SW = OrderedDict()
    con_year_SW[2021] = SW_2021_team
    con_year_SW[2020] = SW_2020_team
    con_year_SW[2019] = SW_2019_team

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
        contestData["subTitle"] = data[6]
        contestData["contestSort"] = data[1]
        award = data[5].split()
        if len(award) > 1:
            award = award[1]
        else:
            award = data[5]
        contestData["award"] = award #중간만 따서 해야댐
        contestData["year"] = data[2]
        contestData["img"] = data[8]

        con_detail = OrderedDict()
        contestData["infoDetail"] = con_detail
        con_detail["awardDetail"] = data[5]

        con_detail["summary"] = data[7]

        con_detail["people"] = []
        peo = ""
        for i in range(9,13):
            if data[i] != None:
                peo += data[i] + ", "
        peo = peo[:-1]

        contestData["people"] = peo

        con_detail["calendar"] = []
        x = data[13].split(",")
        for y in x:
            z = y.strip()
            con_detail["calendar"].append(z)

        con_detail["gitLink"] = data[14]
        con_detail["youtubuLink"] = data[15]
        con_detail["serviceLink"] = data[16]
        con_detail["skills"] = data[17]


        locals()[str(data[1]) + "_" + str(data[2]) + "_team"][data[3]] = contestData

    # Print JSON
    with open('testforios.json', 'w', encoding="utf-8") as make_file:
        json.dump(con_department, make_file, ensure_ascii=False, indent="\t")

makejson(None,None,None)