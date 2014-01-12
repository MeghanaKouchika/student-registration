from django.contrib import admin
from student_registration.models import UserAccount,Attendance,Points,Behavior

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Attendance)
admin.site.register(Points)
admin.site.register(Behavior)
