from django.conf.urls import patterns, include, url

from django.contrib import admin
from student_registration.models import UserAccount,Attendance,Points,Behavior
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_user_account/', 'student_registration.views.create_user_account', name='create_user_account'),
    url(r'^update_attendance/', 'student_registration.views.update_attendance', name='update_attendance'),
    url(r'^update_points/', 'student_registration.views.update_points', name='update_points'),
                       
)
