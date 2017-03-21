from django.conf.urls import url
from . import views

app_name = 'Cbrowser'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #dept cources
    #Cbrowser/number/
    url(r'^(?P<d_id>[0-9]+)/$' , views.detail , name='detail' ),
    #Cbrowser/number/number
    url(r'^(?P<d_id>[0-9]+)/(?P<c_id>[0-9]+)/$' , views.coursePg , name='coursePg' ),
    url(r'^prof/(?P<p_id>[0-9]+)/$' , views.profDet , name='prof' ),
    url(r'course/add/$', views.AddCourse, name='add_cor'),
    url(r'course/Dept/$', views.AddDept, name='add_dept'),
    url(r'^course/(?P<d_id>[0-9]+)/(?P<c_id>[0-9]+)/enroll/$' , views.enrollView , name='enroll'),
    url(r'^student/$' , views.allstu , name='student'),
    url(r'^student/(?P<s_id>[0-9]+)/$' , views.studet , name='studet'),
    url(r'^student/signup$' , views.StuSignUp , name='stusign'),
    url(r'^course/(?P<s_id>[0-9]+)/(?P<c_id>[0-9]+)/unenroll/$',views.UnEnroll,name='unenroll'),
    url(r'^student/edit/(?P<s_id>[0-9]+)/$' , views.studentUpdate , name='sUpdate'),
    url(r'^prof/add/$', views.AddProf, name = 'AddAsProf'),
    url(r'^course-all/$',views.allCourses, name = 'AllCor'),
    url(r'^prof-all/$',views.allProf, name = 'AllPro'),
    url(r'^course/(?P<d_id>[0-9]+)/(?P<c_id>[0-9]+)/addlink/$' , views.addlink , name='addlink'),
    url(r'^ERD/$', views.ERD , name='ER')

]
