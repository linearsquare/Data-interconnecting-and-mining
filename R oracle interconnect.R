--��¼
http://10.17.27.174:8787/auth-sign-in

--��ȡoracle����
library("DBI");
library("ROracle");
drv = dbDriver("Oracle");
con = dbConnect(drv,"kangguangliang1","yhd123,",dbname = "10.0.1.226:1521/edwstd01");
str_sql = 'select * from wuwei.kanggl_data_model0_1';
rs = dbSendQuery(con,str_sql);
data_model0_1 = fetch(rs);
dbDisconnect(con);


--ִ��sql���
dbSendQuery(con ,sql);
dbCommit(con);