"""import sqlite3
connection = sqlite3.connect("table1.db")
cursor = connection.cursor()
#for select -- fetchall()/fetchone()
#for insert,update,delete -- connection.commit()
cursor.execute("SELECT * FROM practice")
print(cursor.fetchall())"""

#sql retrieving data from table
"""
SELECT * FROM practice;
SELECT name,city FROM practice;
SELECT DISTINCT city FROM practice;
SELECT name,city,commission FROM practice WHERE commission>0.13;
SELECT cust_name,city FROM practice WHERE city='London';
SELECT ord_no,purch_amt FROM practice WHERE purch_amt>1000;
SELECT ord_no,purch_amt,ord_date FROM practice WHERE purch_amt BETWEEN 100 AND 1000;
SELECT cust_name,city FROM practice WHERE city IN ('London','New York');
SELECT name,city FROM practice WHERE city<>'Paris';
SELECT name,city FROM practice WHERE city LIKE 'L%';
SELECT name,city,commission FROM practice WHERE commission BETWEEN 0.12 AND 0.15;
SELECT ord_no,purch_amt,ord_date FROM practice WHERE ord_date='2012-10-05';
SELECT cust_name,city,grade FROM practice WHERE grade>=200;
SELECT name,city,commission FROM practice WHERE commission<>0.13;
SELECT name,city,commission FROM practice WHERE commission>0.12 AND city='Paris';
SELECT name,city,commission FROM practice WHERE city IN ('Paris','Rome') AND commission>0.12;
SELECT name,city,commission FROM practice WHERE city NOT IN ('Paris','London');
SELECT name,city FROM practice WHERE city LIKE '%o%';
SELECT name,city FROM practice WHERE city LIKE '%n';
SELECT name,city,commission FROM practice WHERE commission>0.13 OR city='London';
SELECT name,city,commission FROM practice WHERE commission>0.12 AND commission<0.15;
SELECT name,city,commission FROM practice WHERE commission IN (0.13,0.15);
SELECT ord_no,purch_amt,ord_date FROM practice WHERE purch_amt<500;
SELECT cust_name,city,grade FROM practice WHERE grade BETWEEN 100 AND 300;
SELECT pro_name,pro_price FROM practice WHERE pro_price>500;
SELECT pro_name,pro_price FROM practice WHERE pro_price BETWEEN 500 AND 3000;
SELECT DISTINCT salesman_id FROM practice;
SELECT cust_name,grade FROM practice;
SELECT ord_no,purch_amt FROM practice WHERE purch_amt<>2480.40;
"""