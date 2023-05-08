import requests
import json

def getKey(appName):
    # 定义请求头和请求体
    headers = {'Content-Type': 'application/json', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0Z3QiOiJUR1QtZWIxM2NiZmItYTliMy00ZmY2LTg0NjktNGVlOTJhNTU1YzJiIiwibG9naW5Vc2VyIjoie1widW5pcXVlSWRcIjo2MDc5MTEyNTY4MTY0ODg0NDgsXCJ1dWlkXCI6XCJNN0FZMTdQU1wiLFwidWlkXCI6MTc2MTcsXCJ1c2VyTmFtZVwiOlwibWF4LnpoYW5nXCIsXCJyZWFsTmFtZVwiOlwi5byg6b6Z5LmdXCJ9In0.okARZmJ1pqh8RvuaxoL06i5UlJrsVRfy8cGo13qUMYc'}
    data = {'appTitleLike': appName, 'currentPage': 1, 'pageSize': '10'}

    # 发送POST请求并获取响应
    url = 'https://asset-gateway.i.xgimi.com/inner/app/info/pageQuery'
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 解析响应并转换为JSON格式
    response_data = json.loads(response.text)

    # jsonpath: data.data[0].searchPinyin[0]
    key = response_data['data']['data'][0]['searchPinyin'][0]
    return key


appName = '看图识动物（一）'
appNameList = ['360电视卫士', 'CIBN聚精彩', 'WIFI信号神器', '百度电视助手', '宝宝学水果', '贝瓦儿歌', '电视加速器', '电视淘宝', '电视应用管家', '哈利唱儿歌', '哈利的农场', '哈利讲故事', '哈利学数学', '哈利学英语', '嗨健身', '海豚英语', '和彩云', '吉历日历万年历', '驾考宝典', '今今乐道', '开唛K歌', '看图识动物（一）', '莱莱吃水果', '利学语文', '美食杰TV版', '咪咕爱唱', '魔法花园', '莫比健身', '墨迹天气TV版', '亲宝儿歌', '蜻蜓FM', '思维魔方2: 色彩分类', '腾讯电视管家', '万年历', '网络优化大师', '西游奇遇记', '小呆数盒子', '心理FM', '易趣早教', '优化大师', '游戏加速', '智象极速识字']

# 打印JSON格式的响应
for appName in appNameList:
    print(getKey(appName))