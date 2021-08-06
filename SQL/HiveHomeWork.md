## 题目1

```SQL
SELECT t_user.age,-- 年龄段
       sum(t_rate.rate)/count(DISTINCT t_rate.userid) -- 平均分
FROM
  (SELECT userid,
          rate
   FROM hive_sql_test1.t_rating
   WHERE movieid = 2116 ) t_rate
LEFT JOIN t_user t_user ON t_user.userid = t_rate.userid
GROUP BY t_user.age
```
![这是图片](/Users/dongqiudi/PycharmProjects/leetcode-bbbbrent/SQL/p1.png "Magic Gardens")
