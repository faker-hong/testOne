salary    (id, employee_id, amount, pay_date)
employee  (employee_id, department_id)

需求：对部门的各月薪资水平评级，高于当月所有薪资平均值的为higher， 低于为lower，相等为same

1.先求出每个月的公司的平均薪资，评判标准 7000, 8333
SELECT DATE_FORMAT(pay_date,'%Y-%m') pay_date, AVG(amount) standard
FROM salary
GROUP BY pay_date


2.再求出每个部门的每个月平均薪资
SELECT e.department_id, DATE_FORMAT(s.pay_date,'%Y-%m') pay_date, AVG(s.amount)
FROM employee_2 e, salary s
WHERE e.employee_id = s.employee_id
GROUP BY e.department_id, pay_date



3.评级
SELECT department_salary.pay_date, department_salary.department_id,
				(CASE
				WHEN department_salary.amount-company_salary.standard > 0 THEN 'higher'
				WHEN department_salary.amount-company_salary.standard < 0 THEN 'lower'
				ELSE 'same'
				END) comparison
FROM (SELECT e.department_id, DATE_FORMAT(s.pay_date,'%Y-%m') pay_date, AVG(s.amount) amount
			FROM employee e, salary s
			WHERE e.employee_id = s.employee_id
			GROUP BY e.department_id, pay_date) department_salary
LEFT JOIN 
			(SELECT DATE_FORMAT(pay_date,'%Y-%m') pay_date, AVG(amount) standard
			FROM salary
			GROUP BY pay_date
			) company_salary
ON department_salary.pay_date = company_salary.pay_date