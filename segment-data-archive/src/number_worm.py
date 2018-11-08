from utils import initMysql, getByAid

# 起始 和 终止 AID
startAid = 1190000016801859
endAid = 1190000016900000

connect = initMysql()

for aid in range(startAid, endAid):
    getByAid(aid, connect)
