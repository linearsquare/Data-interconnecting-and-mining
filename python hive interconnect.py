#创建链接至hive生产数据集
import pyhs2

conn = pyhs2.connect(host='10.17.28.173',port=10000,authMechanism="PLAIN",
user='kangguangliang1',password='yhd123@',database='default')

cur = conn.cursor()

#展示数据库
print cur.getDatabases()

#执行sql
cur.execute("select * from table")

#返回列信息
print cur.getSchema()

#获取表数据
data = cur.fetch()

#关闭链接
cur.close()
conn.close() 

