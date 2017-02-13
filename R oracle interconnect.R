--登录
http://10.17.27.174:8787/auth-sign-in

--读取oracle数据
library("DBI");
library("ROracle");
drv = dbDriver("Oracle");
con = dbConnect(drv,"kangguangliang1","yhd123,",dbname = "10.0.1.226:1521/edwstd01");
str_sql = 'select * from wuwei.kanggl_data_model0_1';
rs = dbSendQuery(con,str_sql);
data_model0_1 = fetch(rs);
dbDisconnect(con);


--执行sql语句
dbSendQuery(con ,sql);
dbCommit(con);