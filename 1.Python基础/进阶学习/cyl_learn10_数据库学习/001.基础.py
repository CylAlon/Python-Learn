"""
sudo server mysql start 打开数据库
                   restart 重启
ps-ajs|grep mysql 检测


NOT NULL 非空约束
PRIMARY KEY 主键
UNIQUE KEY 唯一约束
DEFAULT 默认约束
FOREIGN KEY 外键

#  linux下命令
select version() 查看版本
select now() 查看当前的时间


-- 链接数据库
    mysql -uroot -pmysql

    不显示密码
    mysql -uroot -p
    mysql
    退出数据库
    exit
    quit
    ctrl + d
创建数据库
create database MyPythonDB
查看创建数据库的命令
SHOW CREATE DATABASE mypythondb
创建带编码的数据库
CREATE DATABASE mypythondb CHARACTER SET utf8 COLLATE utf8_general_ci;

删除数据库
drop database MyPythonDB
    查看当前使用的数据库
    select database();


    -查看所有数据库
    show databases;
    -- 使用数据库
    -- use 数据库的名字
    use python_db1;

    查看所有的表
    show tables


创建表
use pythondb;
create table students(

    id int UNSIGNED PRIMARY KEY auto_increment,
    name VARCHAR(20) not null,
    age TINYINT(1),
    hight DECIMAL(3,2),  # 3个数字2个小数点
    gender enum('男','女')
);
添加字段
  alter table students add witdh DECIMAL(2);
修改字段  width 改为 widths 类型两位长度为3
  alter table students change witdh witdhs DECIMAL(3);
修改数据类型
  alter table students modify witdhs int not null;
删除字段
  alter table student drop widths;
删除表
  droop table students


插入数据
    全插入：
    insert into students values(1, 'python20', 70);
    部分插入：
    insert into students(id, name) values(null, '张三');
    多行插入：如果id是主动增长 则可以写null
    insert into students values(null, '欧阳铁娃', 18, 1.78, '妖', 1),(null, '诸葛铁锤', 18, 1.78, '妖', 1);
删除数据
    delete from students where id = 2;
修改数据
    全修改：
    update students set age = 18;
    按条件修改：
    update students set age = 88 where name = '张三';
    update students set high = 1.2 , gender='男' where name='张三';
查找数据
    全查找：
    select * from students;
    按条件查找：
    select * from students where name='张三';
    select id as di,age from students where id = 2;


"""







