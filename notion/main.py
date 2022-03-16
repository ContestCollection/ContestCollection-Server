from notion.client import NotionClient


token_v2 = "301dc43331e6ef074577002145fa7aac2717142efa9c36a170a53d3d0c9d629994a41f99f9cedd7364aad51134aa95b076c1d159fcf9a8753726c469be776837a55a77794d8ece7acb5e13793ae2"  # 여러분들이 위에서 찾은 토큰을 입력하세요
url = "https://www.notion.so/9cbd2be092c54744afd20b2870a4f89e" #url이랑 웹 토큰

# 노션에 접속해서 url 불러오는 단계
client = NotionClient(token_v2=token_v2)
page = client.get_block(url)


# 노션 접속 후 페이지 정보 가져옴
print("The old title is:", page.title) #얘는 제목

# 얘내는 하위 텍스트들 ex) 표나 텍스트 박스 같은거
for child in page.children:
    if child.type == "table":
        child.get_block()
    elif child.type == "image":
        print(child)
    else:
        print(child.title)

