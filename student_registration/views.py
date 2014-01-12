from django.shortcuts import render
from student_registration.models import *  # imported models with all four classes
from django.http import HttpResponse
import datetime                               #import datetime module
import time                         
# Create your views here.

def create_user_account(request):
    ''' 
    take parameter from url and create user_account in the database
    '''
    if request.method == "GET":
        name = request.GET.get("name", "")         #taking  name value from url
        age = request.GET.get("age", "")
        Class = request.GET.get("class", "")    
        if name and age:
            user_obj = UserAccount()
            user_obj.name = name
            try:
                age = int(age)             #converting age into integer        
            except Exception as e:         #exception raise when age not provide in numbers
                return HttpResponse('Age should be in numbers')
            user_obj.age = age
            user_obj.Class = Class
            user_obj.save()
            return HttpResponse('Account created succesfully')
        else:
            return HttpResponse('Insufficiant parameter provided')
    return HttpResponse('Invalid url')
            
def update_attendance(request):
    '''
    take parameter as student id and update the attendance automatic using system's date and time
    '''
    if request.method == "GET":
        student_id = request.GET.get("student_id", "")
        if student_id:
            try:
                student_id = int(student_id)                     
            except Exception as e:         
                return HttpResponse('student_id should be in numbers')
            user_obj = UserAccount.objects.filter(id = student_id)
            
            if user_obj:
                user_obj = user_obj[0]
                attendance_obj = Attendance.objects.filter(student_id = user_obj)
                
                if not attendance_obj:
                    att_obj = Attendance()
                    att_obj.student_id = user_obj
                else:
                    att_obj = attendance_obj[0]
                    
                att_obj.date = datetime.datetime.now().date()  # assigning system current date 
                att_obj.time = time.strftime('%H:%M:%S')       #assigning system current time
                att_obj.save()
                return HttpResponse('Attendance for student: ' +user_obj.name+ '   updated')
            else:
                return HttpResponse('user dosent exist')
        else:
            return HttpResponse('insufficiant parameter provided')
    return HttpResponse('Invalid url')

def update_points(request):
    '''
    take paramenter student_id and behavior_id and update Points table acordingly
    '''
    if request.method == "GET":
        student_id = request.GET.get("student_id", "")
        behavior_id = request.GET.get("behavior_id", "")
        if student_id and behavior_id:
            try:
                student_id = int (student_id)
                behavior_id = int (behavior_id)
            except Exception as e:         
                return HttpResponse('student_id and behaviour_id should be in numbers')
            user_obj = UserAccount.objects.filter(id = student_id)
            behavior_obj = Behavior.objects.filter(id = behavior_id)
            if user_obj and behavior_obj:
                user_obj = user_obj[0]
                behavior_obj = behavior_obj[0]
                points_obj = Points.objects.filter(student_id = user_obj)
                if not points_obj:
                    point_obj = Points()
                    point_obj.student_id = user_obj
                    point_obj.points = behavior_obj.points               #assigning behaviour points to Points tabl's point
                else:
                    point_obj = points_obj[0]
                    point_obj.points = point_obj.points + behavior_obj.points  # adding points tables point and behaviour points
                point_obj.save()
                return HttpResponse('points for student: ' +user_obj.name+ '   updated')
            else:
                return HttpResponse('user or behaviour dosent exist')
                
        else:
            return HttpResponse('insufficiant parameter provided')
    
    

