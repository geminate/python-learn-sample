import requests
from pyquery import PyQuery as pq
import re
import time

# 起始 和 终止 AID
startAid = 1190000016935062
endAid = 1190000016950000

for aid in range(startAid, endAid):
    try:
        r = requests.get('https://segmentfault.com/a/' + str(aid), timeout=6)
        ht = pq(r.text)

        obj = {
            'title': ht("h1#articleTitle").text(),
            'auth': ht(".article__authormeta strong").text(),
            'catalog': ht(".article__authormeta > a").eq(1).text(),
            'type': re.sub("\s", "", ht(".blog-type-common").attr("data-content")),
            'tag': ht(".tag").text(),
            'hits': re.split(" 次阅读", ht(".content__tech > span").text())[0],
            'read': re.split(" 分钟", re.split("读完需要 ", ht(".content__tech > span").text())[1])[0],
            'votes': ht("#side-widget-votes-num").text(),
            'collect': ht("#mainBookmarkNum").text()
        }
        print(obj)

    except Exception as e:
        print(str(aid))
