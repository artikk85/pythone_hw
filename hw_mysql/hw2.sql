Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 52
Server version: 8.0.25 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables
    -> ;
ERROR 1046 (3D000): No database selected
mysql> use example
Database changed
mysql> show tables;
+-------------------+
| Tables_in_example |
+-------------------+
| users             |
+-------------------+
1 row in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| example            |
| information_schema |
| my_help_keyword    |
| mysql              |
| performance_schema |
| sample             |
| sys                |
| vk                 |
+--------------------+
8 rows in set (0.01 sec)

mysql> ls
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ls' at line 1
mysql> use my_help_keyword
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> exit
Bye

C:\Users\MashkovAV>mysqldump mysql help_keyword --where='true limit 100' > help_keyqord.sql
mysqldump: Couldn't find table: "limit"

C:\Users\MashkovAV>mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 54
Server version: 8.0.25 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> remove example;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'remove example' at line 1
mysql> drop database example, my_help_keyword;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', my_help_keyword' at line 1
mysql> drop database example;
Query OK, 1 row affected (0.08 sec)

mysql> drop database my_help_keyword;
Query OK, 0 rows affected (0.01 sec)

mysql> create database example;
Query OK, 1 row affected (0.01 sec)

mysql> use example;
Database changed
mysql> create table users (
    -> id serial,
    -> name varchar(100) not null unique
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> show tables;
+-------------------+
| Tables_in_example |
+-------------------+
| users             |
+-------------------+
1 row in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| example            |
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| sys                |
| vk                 |
+--------------------+
7 rows in set (0.00 sec)

mysql> exit
Bye

C:\Users\MashkovAV>mysqldump mysql help_keyword--where='order by help_keyword_id limit 100' > help_keyword.sql
mysqldump: Couldn't find table: "help_keyword--where='order"

C:\Users\MashkovAV>mysqldump example > example.sql

C:\Users\MashkovAV>mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 57
Server version: 8.0.25 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database sample;
ERROR 1007 (HY000): Can't create database 'sample'; database exists
mysql> drop database sample;
Query OK, 1 row affected (0.04 sec)

mysql> create database sample;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| example            |
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| sys                |
| vk                 |
+--------------------+
7 rows in set (0.00 sec)

mysql> exit
Bye

C:\Users\MashkovAV>mysql sample < example.sql

C:\Users\MashkovAV>mysqldump mysql help_keyword --where='order by help_keyword_id limit 100' > my_help_keyword.sql
mysqldump: Couldn't find table: "by"

C:\Users\MashkovAV>mysqldump mysql help_keyword --where='true order by help_keyword_id limit 100' > my_help_keyword.sql
mysqldump: Couldn't find table: "order"

C:\Users\MashkovAV>