"""import sqlite3
connection = sqlite3.connect("table1.db")
cursor = connection.cursor()
#for select -- fetchall()/fetchone()
#for insert,update,delete -- connection.commit()
cursor.execute("SELECT * FROM practice")
print(cursor.fetchall())"""

#sql retrieving data from table
#uses table practice from file table1.db
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
SELECT name,city FROM practice WHERE city LIKE '%i%';
SELECT name,city FROM practice WHERE city LIKE '%i__'; #last 3rd is 'i' then only 2 letters
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
SELECT * FROM practice LIMIT 0,5;
SELECT COUNT(pro_id) FROM practice;
SELECT MAX(pro_price) FROM practice;
SELECT MIN(pro_price) FROM practice;
SELECT AVG(pro_price) FROM practice
SELECT COUNT(customer_id) FROM (SELECT customer_id FROM practice GROUP BY customer_id HAVING COUNT(grade)>=1)
SELECT city,MAX(grade) FROM practice GROUP BY city
SELECT customer_id,ord_date,MAX(purch_amt) FROM practice GROUP BY customer_id,ord_date
SELECT salesman_id,purch_amt FROM practice WHERE ord_date='2012-08-17' GROUP BY salesman_id 
SELECT customer_id,MAX(purch_amt) FROM practice WHERE customer_id BETWEEN 3002 AND 3007 GROUP BY customer_id HAVING MAX(purch_amt)>1000
SELECT city,COUNT(salesman_id) FROM practice WHERE source_type='salesman' GROUP BY city
SELECT emp_dept,COUNT(emp_idno) FROM practice WHERE source_type='emp_details' GROUP BY emp_dept
"""

#uses table 2 specifically for orerby,groupby,,agg func
#sorting and filtering hr
"""
SELECT first_name ||' '|| last_name AS full_name,salary FROM employees WHERE salary<6000
SELECT first_name||' '||last_name as full_name FROM employees WHERE first_name NOT LIKE '%M%' ORDER BY department_id
SELECT * FROM employees WHERE (salary BETWEEN 8000 AND 12000 AND commission_pct IS NOT NULL) OR hire_date>'2003-06-05' AND department_id NOT IN (40,120,70)) #considering both date col and given date in iso format i.e. yyyy-mm-dd
SELECT first_name||' '||last_name AS full_name,salary FROM employees WHERE salary NOT BETWEEN 7000 AND 15000 ORDER BY first_name||' '||last_name ASC
SELECT first_name||' '||last_name AS full_name,employee_id,hire_date FROM employees WHERE hire_date BETWEEN '2007-11-05' AND '2009-07-05'
SELECT * FROM employees WHERE (first_name LIKE '%D%') OR (first_name LIKE '%S%') OR (first_name LIKE '%N%')
SELECT first_name||' '||last_name,commission_pct,email,REPLACE(phone_number,'.','-') AS phone_number,salary FROM employees WHERE salary>11000 AND phone_number LIKE '______3%' ORDER BY first_name DESC
SELECT employee_id FROM job_history GROUP BY employee_id HAVING COUNT(*)=2
SELECT employee_id FROM job_history WHERE employee_id LIKE '2%' GROUP BY employee_id HAVING COUNT(*)=2
SELECT job_id,COUNT(*) AS count,SUM(salary) AS sum,MAX(salary)-MIN(salary) AS salary_difference FROM employees GROUP BY job_id
SELECT job_id FROM job_history WHERE start_date-end_date>300 GROUP BY job_id HAVING COUNT(*)>=2
SELECT country_id,COUNT(city) FROM locations GROUP BY country_id
SELECT manager_id,COUNT(employee_id) FROM employees GROUP BY manager_id
SELECT department_id,AVG(salary) FROM employees WHERE commission_pct IS NOT NULL GROUP BY department_id
SELECT DISTINCT department_id FROM employees GROUP BY department_id, manager_id HAVING COUNT(employee_id) >= 4;
SELECT department_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY department_id HAVING COUNT(employee_id)>10
SELECT job_id,AVG(salary) FROM employees GROUP BY job_id HAVING AVG(salary)>8000
#now below 2 query have problem when end_date or * would mean you want to select 1 value for whole group which is 
#impossible to select as a single employee_id can have multiple end_date because of multiple jobs and same multiple col
#values for 2nd query when we write * so which should it select, thats why its better to have only gtoupby col and a agg func
#after select ,the only case it might work is when you write HAVING COUNT(*)=1 as then sql can select values of that record only
SELECT employee_id,end_date FROM job_history GROUP BY employee_id HAVING COUNT(*)>1
SELECT * FROM jobs GROUP BY job_id HAVING COUNT(*)=1 ORDER BY job_title DESC
"""
