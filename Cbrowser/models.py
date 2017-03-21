from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=250)
    c_id = models.IntegerField(primary_key=True)
    semester = models.IntegerField()
    duration = models.IntegerField()
    dept = models.ForeignKey('department', on_delete=models.CASCADE)
    c_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Cbrowser:detail', kwargs={'pk': self.pk})

class prof(models.Model):
    name = models.CharField(max_length=250)
    c_taken = models.ForeignKey('course',on_delete=models.SET_NULL,null=True)
    p_id = models.IntegerField(primary_key=True)
    dept = models.ForeignKey('department',on_delete=models.CASCADE)
    p_pic = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class department(models.Model):
    num_c_off = models.IntegerField()
    dept_name = models.CharField(max_length=250)
    d_id = models.IntegerField(primary_key=True)
    d_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.dept_name

class student(models.Model):
    name = models.CharField(max_length=250)
    s_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gpa = models.FloatField(default=0.0)
    dp = models.CharField(max_length=1000, default='https://thebenclark.files.wordpress.com/2014/03/facebook-default-no-profile-pic.jpg')
    def __str__(self):
        return self.name

class enrollments(models.Model):
    c_id = models.ForeignKey('course')
    s_id = models.ForeignKey('student')
    def __str__(self):
        return self.c_id.name
        
class pastEnrolls(models.Model):
    c_id = models.ForeignKey('course')
    s_id = models.ForeignKey('student')
    def __str__(self):
        return self.c_id.name

class links(models.Model):
    link = models.CharField(max_length=1000)
    c_id = models.ForeignKey('course')
    l_title = models.CharField(max_length=250 , default="NULL")



"""
--
-- Create model enrollments
--
CREATE TABLE "Cbrowser_enrollments" ("id" integer NOT NULL PRIMARY KEY AUTOINCRE
MENT, "c_id_id" integer NOT NULL REFERENCES "Cbrowser_course" ("c_id"));
--
-- Create model links
--
CREATE TABLE "Cbrowser_links" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"link" varchar(1000) NOT NULL, "c_id_id" integer NOT NULL REFERENCES "Cbrowser_c
ourse" ("c_id"));
--
-- Create model prof
--
CREATE TABLE "Cbrowser_prof" ("name" varchar(250) NOT NULL, "p_id" integer NOT N
ULL PRIMARY KEY, "p_pic" varchar(1000) NOT NULL, "c_taken_id" integer NULL REFER
ENCES "Cbrowser_course" ("c_id"), "dept_id" integer NOT NULL REFERENCES "Cbrowse
r_department" ("d_id"));
--
-- Create model student
--
CREATE TABLE "Cbrowser_student" ("name" varchar(250) NOT NULL, "s_id" integer NO
T NULL PRIMARY KEY, "age" integer NOT NULL);
--
-- Add field s_id to enrollments
--
ALTER TABLE "Cbrowser_enrollments" RENAME TO "Cbrowser_enrollments__old";
CREATE TABLE "Cbrowser_enrollments" ("id" integer NOT NULL PRIMARY KEY AUTOINCRE
MENT, "c_id_id" integer NOT NULL REFERENCES "Cbrowser_course" ("c_id"), "s_id_id
" integer NOT NULL REFERENCES "Cbrowser_student" ("s_id"));
INSERT INTO "Cbrowser_enrollments" ("id", "c_id_id", "s_id_id") SELECT "id", "c_
id_id", NULL FROM "Cbrowser_enrollments__old";
DROP TABLE "Cbrowser_enrollments__old";
CREATE INDEX "Cbrowser_links_4d6ad581" ON "Cbrowser_links" ("c_id_id");
CREATE INDEX "Cbrowser_prof_439f5d34" ON "Cbrowser_prof" ("c_taken_id");
CREATE INDEX "Cbrowser_prof_b5a9fd30" ON "Cbrowser_prof" ("dept_id");
CREATE INDEX "Cbrowser_enrollments_4d6ad581" ON "Cbrowser_enrollments" ("c_id_id
");
CREATE INDEX "Cbrowser_enrollments_8ff199ea" ON "Cbrowser_enrollments" ("s_id_id
");
--
-- Add field dept to course
--
ALTER TABLE "Cbrowser_course" RENAME TO "Cbrowser_course__old";
CREATE TABLE "Cbrowser_course" ("name" varchar(250) NOT NULL, "c_id" integer NOT NULL PRIMARY KEY, "semester" integer NOT NULL, "duration" integer NOT NULL, "c_logo" varchar(1000) NOT NULL, "dept_id" integ
er NOT NULL REFERENCES "Cbrowser_department" ("d_id"));
INSERT INTO "Cbrowser_course" ("name", "c_id", "semester", "duration", "c_logo", "dept_id") SELECT "name", "c_id", "semester", "duration", "c_logo", NULL FROM "Cbrowser_course__old";
DROP TABLE "Cbrowser_course__old";
CREATE INDEX "Cbrowser_course_b5a9fd30" ON "Cbrowser_course" ("dept_id");
COMMIT;
"""