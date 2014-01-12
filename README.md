student-registration
====================

a small test webapp in django

It consist basically 3 urls

1) http://127.0.0.1:8000/create_user_account/
 
  we have to provide compulsory two parameter name and age 
  and third parameter class is optional

 for example:
 http://127.0.0.1:8000/create_user_account/?name=krishna&age=24

2) http://127.0.0.1:8000/update_attendance/
   we have to provide compulsory one parameter student id
   for example:
       http://127.0.0.1:8000/update_attendance/?student_id=1

3) http://127.0.0.1:8000/update_points/
   
    we have to provide compulsory two parameter student_id and behaviour_id 
      for example:
      http://127.0.0.1:8000/update_points/?student_id=2&behavior_id=2
      
  