import requests
from utils import initMysql, getByAid
from pyquery import PyQuery as pq

connect = initMysql()


def getUrl(i, element):
    aid = pq(element).attr("href").split("/")[2]
    getByAid(aid, connect)


# 起始 和 终止 page
startPage = 1
endPage = 50

for page in range(startPage, endPage):
    print("----------- PAGE " + str(page) + " ------------")
    r = requests.get('https://segmentfault.com/blogs/newest?page=' + str(page), timeout=10)
    ht = pq(r.text)
    ht(".stream-list__item h2 a").each(getUrl)
