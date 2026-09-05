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

#sql joins and sql join in hr database
#table3
"""
SELECT s.name,c.cust_name,c.city FROM salesman s INNER JOIN customer c on s.city=c.city
SELECT o.ord_no,o.purch_amt,c.cust_name,c.city FROM customer c INNER JOIN (SELECT * FROM orders WHERE purch_amt BETWEEN 500 AND 2000) AS o on c.customer_id=o.customer_id
SELECT c.cust_name,c.city,s.salesman_id,s.commission FROM customer c INNER JOIN salesman s on c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,c.salesman_id,s.commission FROM customer c INNER JOIN (SELECT * FROM salesman WHERE commission>0.12) AS s on c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,s.salesman_id,s.city,s.commission FROM customer c INNER JOIN (SELECT * FROM salesman WHERE commission>0.12) AS s on c.salesman_id=s.salesman_id WHERE c.city<>s.city
SELECT o.ord_no,o.ord_date,o.purch_amt,c.cust_name as 'Customer',c.grade,s.name as 'Salesman',s.commission FROM orders o INNER JOIN customer c on o.customer_id=c.customer_id INNER JOIN salesman s on o.salesman_id=s.salesman_id
SELECT * FROM orders NATURAL JOIN customer NATURAL JOIN salesman
SELECT c.cust_name,c.city,c.grade,s.name,s.city FROM (SELECT * FROM customer WHERE grade<300) AS c INNER JOIN salesman s ON c.salesman_id=s.salesman_id ORDER BY c.customer_id ASC
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM customer c LEFT JOIN orders o ON c.customer_id=o.customer_id ORDER BY o.ord_date ASC
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt,s.name,s.commission FROM customer c LEFT JOIN orders o ON c.customer_id=o.customer_id LEFT JOIN salesman s ON c.salesman_id=s.salesman_id
SELECT * FROM salesman s LEFT JOIN customer c ON c.salesman_id = s.salesman_id ORDER BY s.name;
SELECT c.cust_name,c.city,c.grade,o.ord_no,o.ord_date,o.purch_amt FROM customer c LEFT JOIN orders o on c.customer_id=o.customer_id FULL OUTER JOIN salesman s on s.salesman_id=c.salesman_id 
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c LEFT JOIN (SELECT * FROM orders WHERE purch_amt>=2000) AS o ON c.customer_id=o.customer_id FULL OUTER JOIN salesman s ON c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM customer c RIGHT JOIN orders o ON c.customer_id=o.customer_id
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c RIGHT JOIN orders o ON c.customer_id=o.customer_id
SELECT * FROM customer CROSS JOIN salesman
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) CROSS JOIN (SELECT * FROM salesman WHERE city IS NOT NULL)
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c CROSS JOIN (SELECT * FROM salesman WHERE city IS NOT NULL) AS s WHERE s.city<>c.city
SELECT * FROM company_mast AS c CROSS JOIN item_mast AS i WHERE c.com_id=i.pro_com
SELECT i.pro_name,i.pro_price,c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com
SELECT AVG(i.pro_price),c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com GROUP BY c.com_name
SELECT AVG(i.pro_price),c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com GROUP BY c.com_name HAVING AVG(i.pro_price)>=350
#next two are 2 ways to same question
SELECT a.pro_name,b.mostexp,a.acomname FROM (SELECT c.com_name AS acomname,i.pro_name,i.pro_price AS acompprice FROM company_mast AS c INNER JOIN item_mast AS i ON c.com_id=i.pro_com) AS a INNER JOIN (SELECT MAX(i.pro_price) AS mostexp,c.com_name AS bcomname FROM company_mast AS c INNER JOIN item_mast AS i ON c.com_id=i.pro_com GROUP BY c.com_name) AS b on a.acompprice=b.mostexp AND a.acomname=b.bcomname
SELECT A.pro_name, A.pro_price, F.com_name FROM item_mast A INNER JOIN company_mast F ON A.pro_com = F.com_id AND A.pro_price = (SELECT MAX(A.pro_price) FROM item_mast A WHERE A.pro_com = F.com_id)
SELECT d.dpt_name FROM (SELECT emp_dept FROM emp_details GROUP BY emp_dept HAVING COUNT(*)>2) AS e INNER JOIN emp_department AS d on e.emp_dept=d.dpt_code
SELECT c.cust_name FROM customer c LEFT JOIN orders o ON c.customer_id = o.customer_id WHERE o.customer_id IS NULL;
SELECT d.department_name,e.first_name || ' ' || e.last_name AS full_name FROM departments d INNER JOIN employees e ON d.manager_id = e.employee_id;
#table 2 (self join)
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e JOIN employees m ON m.employee_id=e.manager_id                                     # employee - manager pair
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id                                # match + employee without manager
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e RIGHT JOIN employees m ON m.employee_id=e.manager_id                               # match + manager without employee
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id WHERE e.manager_id IS NULL     # employee without manager
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e RIGHT JOIN employees m ON m.employee_id=e.manager_id WHERE m.employee_id IS NULL   # manager without employee
SELECT e.first_name,e.last_name,e.department_id FROM employees AS e INNER JOIN (SELECT * FROM employees WHERE last_name='Taylor') AS m on m.department_id=e.department_id
#non-equi/range join
#table 2's employee and a new table 
#job_grade
------------+-----------+ -----------
GRADE_LEVEL | LOWEST_SAL|HIGHEST_SAL 
------------+-----------+ -----------
A              1000        2999
B              3000        5999
C              6000        9999
D             10000       14999
E             15000       24999
F             25000       40000

SELECT e.first_name,e.last_name,e.salary,j.grade_level FROM employees e INNER JOIN job_grade j ON e.salary BETWEEN j.lowest_sal AND j.highest_sal
"""

#sql CASE,WHEN,THEN,ESLE,END,combining query results (union/union all etc)
"""
#CASE,WHEN,THEN,ESLE,END use table 2
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN 'high' WHEN salary BETWEEN 3000 AND 4999 THEN 'medium' ELSE 'low' END AS 'salary_category' FROM employees
SELECT first_name,last_name,department_id,CASE department_id WHEN 100 THEN 'management' WHEN 200 THEN 'technical' WHEN 300 THEN 'support' ELSE 'other' END AS 'department_type' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 'above average' WHEN salary BETWEEN 3000 AND 5000 THEN 'average' ELSE 'below average' END AS 'salary_status' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 0.2*salary WHEN salary BETWEEN 3000 AND 5000 THEN 0.1*salary ELSE 0.05*salary END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 OR department_id=100 THEN 'high priority' ELSE 'normal priority' END AS 'salary_priority' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary IS NOT NULL THEN 'salary available' WHEN salary IS NULL THEN 'salary missing' END AS 'salary_info' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN 'high' WHEN salary<5000 THEN 'low' END AS 'salary_order' FROM employees ORDER BY salary_order ASC
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 AND department_id=100 THEN 0.2*salary WHEN salary>=5000 AND department_id<>100 THEN 0.1*salary ELSE 0 END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN CASE WHEN department_id=100 THEN "high_ management" ELSE "high_staff" END WHEN salary<5000 THEN 'low salary' END AS 'salary_label' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 'high' WHEN salary BETWEEN 3000 AND 5000 THEN 'medium' WHEN salary<3000 THEN 'low'  END AS 'salary_category' FROM employees ORDER BY CASE WHEN salary_category='high' THEN 1 WHEN salary_category='medium' THEN 2 WHEN salary_category='low' THEN 3 END
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN ROUND(0.2*salary,2) WHEN salary BETWEEN 3000 AND 4999 THEN ROUND(0.1*salary,2) WHEN salary<3000 THEN ROUND(0.05*salary,2) END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary IS NULL THEN 'not provided' ELSE salary END AS 'salary_display' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN CASE WHEN salary>=10000 THEN 'very high' ELSE 'high' END WHEN salary<5000 THEN CASE WHEN salary>=3000 THEN 'medium' ELSE 'low' END END AS salary_level FROM employees
SELECT SUM(CASE WHEN salary>=5000 THEN 1 ELSE 0 END) FROM employees
SELECT SUM(CASE WHEN salary>=5000 THEN 1 ELSE 0 END)  as high_salary_count,SUM(CASE WHEN salary<5000 THEN 1 ELSE 0 END) as low_salary_count FROM employees
#combining query results (union/union all etc) use table 3
SELECT salesman_id AS id,name,'salesman' AS label FROM salesman WHERE city='London' UNION SELECT customer_id,cust_name,'customer' FROM customer WHERE city='London'
SELECT customer_id,salesman_id FROM orders UNION SELECT customer_id,salesman_id FROM customer
SELECT salesman_id,city FROM customer UNION ALL SELECT salesman_id,city FROM salesman
SELECT salesman_id,city FROM salesman EXCEPT SELECT salesman_id,city FROM customer
SELECT city FROM salesman INTERSECT SELECT city FROM customer ORDER BY city
SELECT city FROM customer EXCEPT SELECT city FROM salesman UNION SELECT city FROM salesman EXCEPT SELECT city FROM customer
#combining above 2 topics using table 3
#https://www.w3resource.com/sql-exercises/union/sql-union.php
#q4--------------------------------------
SELECT s.name,o3.ord_no,o3.ord_date,o3.salesman_id,"highest" AS label FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MAX(purch_amt) AS mostexp,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostexp AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id 
UNION 
SELECT s.name,o3.ord_no,o3.ord_date,o3.salesman_id,"lowest" FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MIN(purch_amt) AS mostcheap,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostcheap AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id
#q5---------------------------------------
SELECT o3.salesman_id,s.name,o3.ord_no,"highest" AS label,o3.ord_date FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MAX(purch_amt) AS mostexp,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostexp AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id
UNION
SELECT o3.salesman_id,s.name,o3.ord_no,"lowest",o3.ord_date FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MIN(purch_amt) AS mostcheap,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostcheap AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id 
ORDER BY ord_no
#q6---------------------------------------
SELECT s.salesman_id,s.name as salesman_name,CASE WHEN c.cust_name IS NOT NULL THEN cust_name WHEN c.cust_name IS NULL THEN 'NO MATCH' END AS customer_name,s.commission FROM salesman s LEFT JOIN customer c ON s.city=c.city ORDER BY salesman_name DESC
#q7---------------------------------------
SELECT DISTINCT s.salesman_id,s.name as salesman_name,s.city,CASE WHEN c.cust_name IS NOT NULL THEN 'MATCHED' WHEN c.cust_name IS NULL THEN 'NO MATCH' END AS city_match FROM salesman s LEFT JOIN customer c ON s.city=c.city
#q8--------------------------------------
SELECT customer_id,city,grade,"high" AS rating FROM customer WHERE grade>=300 UNION SELECT customer_id,city,grade,"low" AS rating FROM customer WHERE grade<300
#q9--------------------------------------
SELECT c.cust_name AS name,c.customer_id AS id FROM customer c INNER JOIN orders o ON c.customer_id=o.customer_id GROUP BY c.customer_id HAVING COUNT(*)>1 UNION SELECT s.name,s.salesman_id FROM salesman s INNER JOIN orders o ON s.salesman_id=o.salesman_id GROUP BY s.salesman_id HAVING COUNT(*)>1
"""

