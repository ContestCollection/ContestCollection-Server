import json
from collections import OrderedDict


# contestData 파트
contestData = OrderedDict()
contestData["title"] = "Air-Alarm"
contestData["subTitle"] = "미세먼지 및 공기질 측정기"
contestData["prize"] = "2021년 대상, 인기상"
contestData["members"] = ["19학번 손창하", "19학번 고병우", "20학번 박진희", "20학번 김하은"]
contestData["gitLink"] = "https://github.com/Air-Alarm"
contestData["youtubeLink"] = "https://youtu.be/v_4Lv-mid30"
# 각 팀 나누는 파트
team = OrderedDict()
team["team0"] = contestData

# con_year 파트
con_year = OrderedDict()
con_year[2021] = team
con_year[2020] = None

# con_department 파트
con_department = OrderedDict()
con_department["IT"] = con_year
con_department["SW"] = None
con_department["MC"] = None

# Print JSON
with open('test.json', 'w', encoding="utf-8") as make_file:
    json.dump(con_department, make_file, ensure_ascii=False, indent="\t")