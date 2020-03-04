需求：统计员工近三个月工资总和，但不包括最近一个月
结果展示按id升序，按月份降序

1.先求出近三个月工资
SELECT e1.id, e1.Month, SUM(e2.salary) Salary
FROM employee e1, employee e2
WHERE e1.id = e2.id AND e1.Month-e2.Month<=2 AND  e1.Month>=e2.Month -- 两个月份相减不能大于2,且e1的month不小于e2的month
GROUP BY e1.id, e1.month


2.取出最近一个月的数据
SELECT id, MAX(Month) Month
FROM employee
GROUP BY id


3.排除最近一个月后按id升序，工资降序显示结果
SELECT recent_three.id id, recent_three.Month Month, recent_three.Salary Salary
FROM (SELECT e1.id, e1.Month, SUM(e2.salary) Salary
			FROM employee e1, employee e2
			WHERE e1.id = e2.id AND e1.Month-e2.Month<=2 AND  e1.Month>=e2.Month
			GROUP BY e1.id, e1.month
			) recent_three 
LEFT JOIN 
				(SELECT id, MAX(Month) Month
				FROM employee
				GROUP BY id) most_recent
ON recent_three.id = most_recent.id 
WHERE recent_three.Month <> most_recent.Month
ORDER BY recent_three.id, recent_three.Month DESC


