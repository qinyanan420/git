# import pymysql
# db = pymysql.connect(host='192.168.1.123', user='root', passwd='bigfish', db='newbingo', port=3306, charset='utf8')
# cursor = db.cursor()
#
# # sql = 'select * from bingo_mail'
# uid = 3187
# for i in range(100):
#     sql ='INSERT INTO bingo_mail(id, userid, mailid, state) VALUES ("%d", "%d","%d","%d")'%(uid+i,1083924,314,0)
#     cursor.execute(sql)
#     db.commit()
# cursor.close()
# db.close()