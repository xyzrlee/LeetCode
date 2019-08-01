# Write your MySQL query statement below
select a.Id
from Weather a
left join Weather b
on b.RecordDate = subdate(a.RecordDate, 1)
where b.Temperature is not null
  and b.Temperature < a.Temperature