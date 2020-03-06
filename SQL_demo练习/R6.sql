需求：列出2019-1-1到2019-12-31期间成功或失败的持续时段
failed（fail_date）
succeeded(success_date)


1.分开处理之后union ALL后根据end_date排序

失败时段：
SELECT
	IF(DATE_SUB(fail_Date,INTERVAL 1 DAY)=@date, @rank:=@rank, @rank:=@rank+1) group_date,
	@date:=fail_date fail_date
FROM
	failed,
	(SELECT @rank:=0, @date:='') rank
WHERE
	fail_date BETWEEN '2019-01-01' AND '2019-12-31'


成功时段：
SELECT
	IF(DATEDIFF(success_date,@date)=1, @rank:=@rank, @rank:=@rank+1) group_date,
	@date:=success_date success_date
FROM
 succeeded,
(SELECT @rank:=0, @date:='') rank
WHERE
	success_date BETWEEN '2019-01-01' AND '2019-12-31'


合并：
SELECT
	'failed' period_state,
	MIN(fail_date) start_date,
	MAX(fail_date) end_date
FROM
	(SELECT
		IF(DATE_SUB(fail_Date,INTERVAL 1 DAY)=@date, @rank:=@rank, @rank:=@rank+1) group_date,
		@date:=fail_date fail_date
	FROM
		failed,
		(SELECT @rank:=0, @date:='') rank
	WHERE
		fail_date BETWEEN '2019-01-01' AND '2019-12-31') fail_period_state
GROUP BY group_date
UNION ALL
SELECT
	'succeeded' period_state,
	MIN(success_date) start_date,
	MAX(success_date) end_date
FROM
	(SELECT
		IF(DATEDIFF(success_date,@date)=1, @rank:=@rank, @rank:=@rank+1) group_date,
		@date:=success_date success_date
	FROM
	 succeeded,
	(SELECT @rank:=0, @date:='') rank
	WHERE
		success_date BETWEEN '2019-01-01' AND '2019-12-31') success_period_state
GROUP BY group_date


合并完后根据end_date排序：
SELECT
	period_state,
	start_date,
	end_date
FROM
	(SELECT
	'failed' period_state,
	MIN(fail_date) start_date,
	MAX(fail_date) end_date
FROM
	(SELECT
		IF(DATE_SUB(fail_date,INTERVAL 1 DAY)=@date, @rank:=@rank, @rank:=@rank+1) group_date,
		@date:=fail_date fail_date
	FROM
		failed,
		(SELECT @rank:=0, @date:='') rank
	WHERE
		fail_date BETWEEN '2019-01-01' AND '2019-12-31') fail_period_state
GROUP BY group_date
UNION ALL
SELECT
	'succeeded' period_state,
	MIN(success_date) start_date,
	MAX(success_date) end_date
FROM
	(SELECT
		IF(DATE_SUB(success_date,INTERVAL 1 DAY)=@date, @rank:=@rank, @rank:=@rank+1) group_date,
		@date:=success_date success_date
	FROM
	 succeeded,
	(SELECT @rank:=0, @date:='') rank
	WHERE
		success_date BETWEEN '2019-01-01' AND '2019-12-31') success_period_state
GROUP BY group_date
	) period_state
ORDER BY end_date

