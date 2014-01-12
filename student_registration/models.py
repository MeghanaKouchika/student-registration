from django.db import models
import datetime

# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    Class = models.CharField(max_length=200)
    
    def __unicode__(self):  #return name of the object when called
        return self.name

class Attendance(models.Model):
    student_id = models.ForeignKey(UserAccount)
    date = models.DateField('date', auto_now_add = True ,blank = True )
    time = models.CharField(max_length=200)
    def __unicode__(self):  #return name of the object when called
        return self.student_id.name

   
class Points(models.Model):
    student_id = models.ForeignKey(UserAccount)
    points = models.IntegerField(default=0)  #if not prvide take 0 as default
    def __unicode__(self):  #return name of the object when called
        return self.student_id.name

class Behavior(models.Model):
    behavior_name = models.CharField(max_length=200)
    points = points = models.IntegerField(default=0)    #if not prvide take 0 as default
    
    def __unicode__(self):  #return behavior_name of the object when called
        return self.behavior_name
