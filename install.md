## 安装mysql
教程:https://blog.csdn.net/wtfmonking/article/details/17467399
url:https://dev.mysql.com/downloads/windows/installer/

### 创建数据库
create database MovieData;
use MovieData;

### 创建表
CREATE TABLE moviegenre3(imdbId INT NOT NULL PRIMARY KEY,title varchar(300),poster varchar(600)); 

CREATE TABLE users_resulttable(userId INT NOT NULL,imdbId INT,rating DECIMAL(3,1)); 

### 修改mysql配置
`code 'C:\ProgramData\MySQL\MySQL Server 5.7\my.ini'`
添加`secure-file-priv=`
重启mysql 
### 载入数据
load data local infile "C:/Users/yxf/Desktop/MovieRecommend/data/users_resulttable.csv" into table users_resulttable fields terminated by ',' lines terminated by '\n' (userId,imdbId,rating);


LOAD DATA LOCAL INFILE 'C:/Users/yxf/Desktop/MovieRecommend/data/output.csv'
INTO TABLE moviegenre3
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
(imdbId, title, poster);


alter table users_resulttable add column id int auto_increment PRIMARY KEY; 