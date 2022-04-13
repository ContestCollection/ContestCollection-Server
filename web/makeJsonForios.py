import json
from collections import OrderedDict
from DB import getFromDB, getFromDB2

def makejson():

    t = getFromDB()
    #IT인지랑 2021인지랑 등등 체크해야함

    contestData = OrderedDict()
    contestData["headerList"] = []
    year = 2021

    #대상
    prizes = ["대상", "금상", "은상", "동상", "장려상"]

    for prize in prizes:

        prizeData_one = OrderedDict()
        contestData["headerList"].append(prizeData_one)
        prizeData_one["id"] = prizes.index(prize)
        prizeData_one["prizeHeader"] = prize
        prizeData_one["prizeListData"] = []


        detailid = 0
        for i in range(len(t)):
            temp = t[i][5].split()
            if len(temp) != 1:
                if temp[1] == prize and t[i][2] == year:
                    print(t[i])
                    prizeData_one_detail = OrderedDict()
                    prizeData_one_detail["id"] = detailid
                    detailid += 1
                    prizeData_one_detail["name"] = t[i][4]
                    prizeData_one_detail["subTitle"] = t[i][5]
                    prizeData_one_detail["img"] = t[i][8]
                    prizeData_one_detail_info = OrderedDict()
                    prizeData_one_detail_info["awardDetail"] = t[i][5]
                    prizeData_one_detail_info["summary"] = t[i][7]
                    #people 합치는 부분
                    people = ""
                    for ii in range(9, 13):
                        if t[i][ii] != None:
                            people += t[i][ii] + ", "
                    people = people.strip()
                    people = people.strip(",")
                    prizeData_one_detail_info["people"] = people
                    prizeData_one_detail_info["calender"] = t[i][13]
                    prizeData_one_detail_info["gitLink"] = t[i][14]

                    youtube = t[i][15].split("/")
                    if len(youtube) != 1:
                        youtube = youtube[3]
                    else:
                        youtube = youtube[0]

                    prizeData_one_detail_info["youtubeLink"] = youtube
                    prizeData_one_detail_info["serviceLink"] = t[i][16]
                    prizeData_one_detail_info["skills"] = t[i][17]
                    prizeData_one_detail["infoDetail"] = prizeData_one_detail_info
                    prizeData_one["prizeListData"].append(prizeData_one_detail)


    #금상
    prizeData_two = OrderedDict()
    #은상
    prizeData_three = OrderedDict()
    #동상
    prizeData_four = OrderedDict()
    #장려상
    prizeData_five = OrderedDict()





    # Print JSON
    with open('ttap.json', 'w', encoding="utf-8") as make_file:
        json.dump(contestData, make_file, ensure_ascii=False, indent="\t")

makejson()