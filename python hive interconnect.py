#����������hive�������ݼ�
import pyhs2

conn = pyhs2.connect(host='10.17.28.173',port=10000,authMechanism="PLAIN",
user='kangguangliang1',password='yhd123@',database='default')

cur = conn.cursor()

#չʾ���ݿ�
print cur.getDatabases()

#ִ��sql
cur.execute("select * from table")

#��������Ϣ
print cur.getSchema()

#��ȡ������
data = cur.fetch()

#�ر�����
cur.close()
conn.close() 

