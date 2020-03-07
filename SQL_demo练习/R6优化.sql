优化：
1.先将两表合并
SELECT
	'failed' period_state,
	fail_date date
FROM
	failed
WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
UNION ALL
SELECT
	'succeeded' period_state,
	success_date date
from
	succeeded
WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'

2.开始分组
SELECT
	period_state,
	IF(DATEDIFF(date,@before_date)=1, @rank:=@rank, @rank:=@rank+1) rank,
	@before_date:=date date
FROM
	(
	SELECT
		'failed' period_state,
		fail_date date
	FROM
		failed
	WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
	UNION ALL
	SELECT
		'succeeded' period_state,
		success_date date
	from
		succeeded
	WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31') union_date,
	(SELECT @rank:=0, @before_date:='') rank


3.获得每组最大最小值
SELECT
	period_state,
	MIN(date) start_date,
	MAX(date) end_date
FROM
	(SELECT
	period_state,
	IF(DATEDIFF(date,@before_date)=1, @rank:=@rank, @rank:=@rank+1) rank,
	@before_date:=date date
FROM
	(
	SELECT
		'failed' period_state,
		fail_date date
	FROM
		failed
	WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
	UNION ALL
	SELECT
		'succeeded' period_state,
		success_date date
	from
		succeeded
	WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
	) union_date,
	(SELECT @rank:=0, @before_date:='') rank
	) group_date
 GROUP BY rank
ORDER BY start_date





合并符合的日期，根据日期排序
SELECT
'failed' period_state,
fail_date date
FROM failed
WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
UNION ALL
SELECT
'succeeded' period_state,
success_date date
FROM succeeded
WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
order by date


根据状态是否变化来分组
SELECT 
	date,
	IF(period_state=@state, @rank:=@rank, @rank:=@rank+1) rank,
	@state:=period_state period_state
FROM 
	(
	SELECT
		'failed' period_state,
		fail_date date
	FROM failed
	WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
	UNION ALL
	SELECT
		'succeeded' period_state,
		success_date date
	FROM succeeded
	WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
	order by date) order_date,
	(SELECT @state:='', @rank:=0) state




最终结果：
SELECT
	period_state,
	MIN(date) start_date,
	MAX(date) end_date
FROM
	(SELECT 
	date,
	IF(period_state=@state, @rank:=@rank, @rank:=@rank+1) rank,
	@state:=period_state period_state
FROM 
	(
	SELECT
		'failed' period_state,
		fail_date date
	FROM failed
	WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
	UNION ALL
	SELECT
		'succeeded' period_state,
		success_date date
	FROM succeeded
	WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
	order by date) order_date,
	(SELECT @state:='', @rank:=0) state) group_date
GROUP BY rank