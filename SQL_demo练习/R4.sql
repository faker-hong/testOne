需求：找出各个公司的工资中位数
employee(Id, Company, Salary)

1.求出每个人工资在工资内部的排位
SELECT 
	id,
	company,
	salary,
	@order_num:=(CASE WHEN @company_name=company THEN @order_num:=@order_num+1 ELSE @order_num:=1 END) company_no,
	@company_name:=company company_name
FROM 
	(select id,company,salary from employee) company_order,
	(SELECT @order_num:=0, @company_name:='') variable
ORDER BY company, salary
-- 这里对salary也进行group by


2.求出各个公司总共有多少人
SELECT e1.id, e1.company, e1.salary, e2.cnt
FROM employee e1
LEFT JOIN (SELECT company, COUNT(1) cnt FROM employee GROUP BY company) e2
ON e1.company=e2.company



3.找到排序在总数一半的人员信息
SELECT 
	salary_order_by_company.id, 
	salary_order_by_company.company, 
	salary_order_by_company.salary
-- 	salary_order_by_company.company_no, 
-- 	count_company.cnt
FROM 
	(SELECT 
	id,
	company,
	salary,
	@order_num:=(CASE WHEN @company_name=company THEN @order_num:=@order_num+1 ELSE @order_num:=1 END) company_no,
	@company_name:=company company_name
	FROM 
		(select id,company,salary from employee) company_order,
		(SELECT @order_num:=0, @company_name:='') variable
	ORDER BY company, salary) salary_order_by_company
JOIN
	(SELECT e1.id, e1.company, e1.salary, e2.cnt
	FROM employee e1
	LEFT JOIN (SELECT company, COUNT(1) cnt FROM employee GROUP BY company) e2
	ON e1.company=e2.company) count_company
ON salary_order_by_company.id = count_company.id
WHERE salary_order_by_company.company_no >= count_company.cnt/2 and salary_order_by_company.company_no <= count_company.cnt/2 + 1

