需求：
	查询出每天至少一次提交的黑客数量，和提交次数最多的黑客id和姓名，如何提交次数相同则取id小的


1.获取每天不同黑客的提交次数
SELECT 
	submission_date,
	hacker_id,
	COUNT(*) cnt
FROM
	submissions
GROUP BY
	submission_date,
	hacker_id


2.获取每天都提交的黑客数
(SELECT
	s.submission_date,
	COUNT(*) cnt
FROM
	submissions s
GROUP BY
	s.submission_date
LIMIT 1)
UNION ALL
SELECT
	group_date_hacker_1.submission_date,
	COUNT(*) cnt
FROM
	(SELECT 
		submission_date,
		hacker_id,
		COUNT(*) cnt
	FROM
		submissions
	GROUP BY
		submission_date,
		hacker_id) group_date_hacker_1
JOIN 
	(SELECT 
		submission_date,
		hacker_id,
		COUNT(*) cnt
	FROM
		submissions
	GROUP BY
		submission_date,
		hacker_id) group_date_hacker_2
ON DATEDIFF(group_date_hacker_1.submission_date, group_date_hacker_2.submission_date)=1 
		AND group_date_hacker_1.hacker_id in (group_date_hacker_2.hacker_id)
GROUP BY group_date_hacker_1.submission_date


3.获取每天提交次数最多的黑客名和编号,次数相同取id小的
SELECT
	group_date_hacker.submission_date,
	group_date_hacker.hacker_id,
	MAX(cnt)
FROM
	(SELECT
		s.submission_date,
		s.hacker_id,
		COUNT(*) cnt
	FROM
		submissions s
	GROUP BY
		s.submission_date,
		s.hacker_id
	ORDER BY
		s.submission_date,
		cnt DESC,
		s.hacker_id) group_date_hacker
GROUP BY submission_date


4.最终结果
SELECT
	every_hacker_submit.submission_date submission_date,
	every_hacker_submit.cnt every_hacker_submit,
	most_submit.hacker_id,
	hackers.name
FROM
	(SELECT
		group_date_hacker.submission_date,
		group_date_hacker.hacker_id,
		MAX(cnt)
	FROM
		(SELECT
			s.submission_date,
			s.hacker_id,
			COUNT(*) cnt
		FROM
			submissions s
		GROUP BY
			s.submission_date,
			s.hacker_id
		ORDER BY
			cnt DESC,
			s.hacker_id) group_date_hacker
	GROUP BY submission_date) most_submit
LEFT JOIN
	hackers
ON hackers.hacker_id = most_submit.hacker_id
LEFT JOIN
	((SELECT
			s.submission_date,
			COUNT(*) cnt
		FROM
			submissions s
		GROUP BY
			s.submission_date
		LIMIT 1)
		UNION ALL
		SELECT
			group_date_hacker_1.submission_date,
			COUNT(*) cnt
		FROM
			(SELECT 
				submission_date,
				hacker_id,
				COUNT(*) cnt
			FROM
				submissions
			GROUP BY
				submission_date,
				hacker_id) group_date_hacker_1
		JOIN 
			(SELECT 
				submission_date,
				hacker_id,
				COUNT(*) cnt
			FROM
				submissions
			GROUP BY
				submission_date,
				hacker_id) group_date_hacker_2
		ON DATEDIFF(group_date_hacker_1.submission_date, group_date_hacker_2.submission_date)=1 
				AND group_date_hacker_1.hacker_id in (group_date_hacker_2.hacker_id)
		GROUP BY group_date_hacker_1.submission_date) every_hacker_submit
	ON every_hacker_submit.submission_date = most_submit.submission_date

