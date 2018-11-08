import requests
from pyquery import PyQuery as pq
import re
import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='pylearn',
    charset='utf8'
)
cursor = connect.cursor()


def saveToMysql(obj):
    r = cursor.executemany('insert into `segment-data-archive` values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)',
                           [(obj['id'],
                             obj['url'],
                             obj['title'],
                             obj['auth'],
                             obj['catalog'],
                             obj['type'],
                             obj['tag'],
                             obj['hits'],
                             obj['read'],
                             obj['votes'],
                             obj['collect'],
                             obj['content']
                             )])

    # 提交语句
    connect.commit()
    print(obj['id'] + ":  success")


# 起始 和 终止 AID
startAid = 1190000016800000
endAid = 1190000016900000

for aid in range(startAid, endAid):
    try:
        r = requests.get('https://segmentfault.com/a/' + str(aid), timeout=6)
        ht = pq(r.text)

        obj = {
            'id': str(aid),
            'url': 'https://segmentfault.com/a/' + str(aid),
            'title': ht("h1#articleTitle").text(),
            'auth': ht(".article__authormeta strong").text(),
            'catalog': ht(".article__authormeta > a").eq(1).text(),
            'type': re.sub("\s", "", ht(".blog-type-common").attr("data-content")),
            'tag': ht(".tag").text(),
            'hits': re.split(" 次阅读", ht(".content__tech > span").text())[0],
            'read': re.split(" 分钟", re.split("读完需要 ", ht(".content__tech > span").text())[1])[0],
            'votes': ht("#side-widget-votes-num").text(),
            'collect': ht("#mainBookmarkNum").text(),
            'content': ht(".article__content").text()
        }
        saveToMysql(obj)

    except Exception as e:
        print(str(aid) + ":  " + str(e))
