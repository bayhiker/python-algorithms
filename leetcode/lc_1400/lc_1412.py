"""
# https://circlecoder.com/find-the-quiet-students-in-all-exams/
select student_id,student_name 
from student
where student_id in (select student_id from exam) and 
      student_id not in 
        (select student_id 
         from 
            (select student_id, 
                rank() over(partition by exam_id order by score asc) as asc_rank,
                rank() over(partition by exam_id order by score desc) as desc_rank 
             from exam) tab1
        where asc_rank=1 or desc_rank=1)
"""
