from django.http import HttpResponseRedirect, HttpResponse
from . models import *
from . forms import *
from django.db import connection
from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy , reverse


class IndexView(generic.ListView):
    template_name = 'Cbrowser/index.html'
    context_object_name = 'all_dept'

    def get_queryset(self):
        all_dept = department.objects.raw("SELECT * FROM Cbrowser_department")
        # context = {'all_dept' : all_dept,}
        # return render(request , 'Cbrowser/index.html',context)
        return all_dept

def detail(request,d_id):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cbrowser_course WHERE dept_id = %s",[d_id])
        cor = cursor.fetchall()
        cursor.execute("SELECT * FROM Cbrowser_department WHERE d_id = %s",[d_id])
        dpt = cursor.fetchall()
    except cor.DoesNotExist:
        raise Http404("No data 404 ")
    v=0
    return render(request, 'Cbrowser/detail.html',context = {'cor' : cor, 'dpt' : dpt, })

def ERD(request):
    return render(request, 'Cbrowser/ER.html', context=None)

def coursePg(request,d_id, c_id):
    cursor = connection.cursor()
    lnks = links.objects.raw("SELECT * FROM Cbrowser_links WHERE c_id_id = %s", [c_id])
    cursor.execute("SELECT * FROM Cbrowser_course Cbrowser_course WHERE dept_id = %s AND c_id=%s",[d_id,c_id])
    cor=cursor.fetchall()
    cursor.execute("SELECT * FROM Cbrowser_department WHERE d_id = %s",[d_id])
    dpt = cursor.fetchall()
    cursor.execute("SELECT * FROM Cbrowser_prof WHERE dept_id = %s AND c_taken_id = %s",[d_id,c_id])
    prf = cursor.fetchall()
    cursor.execute("SELECT * FROM Cbrowser_enrollments JOIN Cbrowser_student on s_id = s_id_id WHERE c_id_id = %s ",[c_id])
    enrl = cursor.fetchall()
    cursor.execute("SELECT * FROM Cbrowser_pastEnrolls JOIN Cbrowser_student on s_id = s_id_id WHERE c_id_id = %s ",[c_id])
    penrl = cursor.fetchall()
    context = {
        'lnks':lnks,
        'dpt':dpt,
        'cor':cor,
        'prf':prf,
        'enrl':enrl,
        'penrl':penrl
    }
    return render(request, 'Cbrowser/CorDets.html',context = context)


def profDet(request,p_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cbrowser_prof ")
    prf = prof.objects.raw("SELECT * FROM Cbrowser_prof WHERE p_id = %s",[p_id])
    return render(request, 'Cbrowser/ProfDet.html', context = {'prf':prf,})

class CorCreate(CreateView):
    model = course
    fields = ['name','c_id','semester','duration','c_logo','dept']

def enrollView(request,d_id, c_id):
    form = enrollForm(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cbrowser_enrollments ")
        num = cursor.fetchall()
        num = num[-1][0]+1
        cursor.execute("INSERT INTO Cbrowser_enrollments VALUES(%s, %s , %s )",[num,c_id,instance.s_id_id])
        cursor.execute("SELECT * FROM Cbrowser_student ")
        stu = cursor.fetchall()
        context = {
            'stu':stu,
        }
        return HttpResponseRedirect('/Cbrowser/'+str(d_id)+'/'+str(c_id)+'/')
    context = {
        'form':form,
        'cid':c_id,
    }
    return render(request, 'Cbrowser/enroll.html', context=context)

def addlink(request, d_id, c_id):
    form = addLinkForm(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cbrowser_links ")
        num = cursor.fetchall()
        num = num[-1][0]+1
        cursor.execute('INSERT INTO Cbrowser_links VALUES(%s , %s , %s , %s)',[num,instance.link,c_id,instance.l_title])
        return HttpResponseRedirect('/Cbrowser/'+str(d_id)+'/'+str(c_id)+'/')
    context = {
        'form':form,
    }
    return render(request, 'Cbrowser/AddLink.html', context)

def AddCourse(request):
    form = AddCourseForm(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        print([instance.name,instance.c_id,instance.semester,instance.duration,instance.c_logo,instance.dept.d_id])
        cursor.execute("INSERT INTO Cbrowser_course VALUES(%s , %s , %s , %s , %s , %s)",[instance.name,instance.c_id,instance.semester,instance.duration,instance.c_logo,instance.dept.d_id])
        cursor.execute("SELECT COUNT(*) FROM Cbrowser_course WHERE dept_id = %s",[instance.dept.d_id])
        numb = cursor.fetchall()
        newOff = numb[0][0]
        cursor.execute("UPDATE Cbrowser_department SET num_c_off = %s WHERE d_id = %s",[newOff, instance.dept.d_id])
        return HttpResponseRedirect('/Cbrowser/'+str(instance.dept.d_id)+'/')
    context = {
        'form':form,
    }
    return render(request, "Cbrowser/AddCor.html",context)

def AddProf(request):
    form = AddAndAsignProf(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        print([instance.name,instance.c_taken,instance.p_id,instance.dept,instance.p_pic])
        cursor.execute("INSERT INTO Cbrowser_prof VALUES(%s , %s , %s , %s , %s)",[instance.name,instance.p_id,instance.p_pic,instance.c_taken.c_id,instance.dept.d_id])
        return HttpResponseRedirect('/Cbrowser/prof/'+str(instance.p_id)+'/')
    context = {
        'form':form,
    }
    return render(request, "Cbrowser/AddProf.html",context)

def AddDept(request):
    form = AddDeptForm(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Cbrowser_department VALUES(%s , %s , %s , %s )",[0,instance.dept_name,instance.d_id,instance.d_logo])
        return HttpResponseRedirect('/Cbrowser/'+str(instance.d_id)+'/')
    context = {
        'form':form,
    }
    return render(request, "Cbrowser/AddDept.html",context)


def allstu(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cbrowser_student ")
    stu = cursor.fetchall()
    context = {
        'stu':stu,
    }
    return render(request ,'Cbrowser/student.html',context=context)

def studet(request, s_id):
    stu = student.objects.raw("SELECT * FROM Cbrowser_student WHERE s_id = %s",[s_id])
    enrl= enrollments.objects.raw("SELECT * FROM Cbrowser_enrollments WHERE s_id_id = %s",[s_id])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cbrowser_pastEnrolls JOIN Cbrowser_course on c_id = c_id_id WHERE s_id_id = %s ",[s_id])
    penrl = cursor.fetchall()
    context = {
        'stu':stu,
        'enrl':enrl,
        'penrl':penrl,
    }
    return render(request, 'Cbrowser/studet.html', context = context)

def StuSignUp(request):
    form = SignUp(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Cbrowser_student VALUES(%s,%s,%s,%s,%s)",[instance.name,instance.s_id,instance.age,instance.gpa,instance.dp])
        stu = student.objects.raw("SELECT * FROM Cbrowser_student WHERE s_id = %s",[instance.s_id])
        enrl= enrollments.objects.raw("SELECT * FROM Cbrowser_enrollments WHERE s_id_id = %s",[instance.s_id])
        context = {
            'stu':stu,
            'enrl':enrl,
        }
        return render(request, 'Cbrowser/studet.html', context = context)
    context = {
        'form':form
    }
    return render(request, 'Cbrowser/signup.html', context=context)

def studentUpdate(request, s_id):
    form = StudentUpdateForm(request.POST)
    context = {
        'form' : form,
    }
    if form.is_valid():
        data = form.cleaned_data
        data = [v for v in data.values()]
        print("DATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",data)
        cursor = connection.cursor()
        cursor.execute("UPDATE Cbrowser_student SET name = %s , age = %s ,dp = %s , gpa = %s WHERE s_id = %s",[data[0],data[1],data[3],data[2],s_id])
        return HttpResponseRedirect('/Cbrowser/student/'+str(s_id)+'/')
    return render(request,"Cbrowser/StudentUpdate.html",context)


def UnEnroll(request,s_id,c_id):
    print(s_id,c_id)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Cbrowser_enrollments WHERE s_id_id = %s AND c_id_id = %s",[s_id,c_id])
    print("DATA DELETED")
    stu = student.objects.raw("SELECT * FROM Cbrowser_student WHERE s_id = %s",[s_id])
    enrl= enrollments.objects.raw("SELECT * FROM Cbrowser_enrollments WHERE s_id_id = %s",[s_id])
    for e in enrl:
        print(e)
    context = {
        'stu':stu,
        'enrl':enrl,
    }
    print("RETURNING")
    return HttpResponseRedirect('/Cbrowser/student/'+str(s_id)+'/')

def allCourses(request):
    cor = course.objects.raw("SELECT * FROM Cbrowser_course")

    context = {
        'cor' : cor,
    }
    return render(request , "Cbrowser/AllCor.html",context)

def allProf(request):
    pro = prof.objects.raw("SELECT * FROM Cbrowser_prof")
    context = {
        'pro' : pro,
    }
    return render(request , "Cbrowser/AllPro.html",context)
