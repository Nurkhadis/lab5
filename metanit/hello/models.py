from django.db import models


class courses(models.Model):
    CourseName = models.TextField()
    CourseDesc = models.TextField()
    Credits = models.BigIntegerField()
    DeptID = models.TextField()

class students(models.Model):
    LastName = models.TextField()
    FirstName = models.TextField()
    MiddleName = models.TextField()
    Addr1 = models.TextField()
    Addr2 = models.TextField()
    City = models.TextField()
    StateProvince = models.TextField()
    Country = models.TextField()
    PostalCode = models.TextField()
    Email = models.TextField()

#class stuclasses(models.Model):
 #   ClassID = models.ForeignKey(classes, on_delete = models.CASCADE)
  #  StudentID = models.ForeignKey(students, on_delete = models.CASCADE)
   # Grade = models.ForeignKey(GradeValues, on_delete = models.CASCADE)

class GradeValues(models.Model):
    QGrade = models.DecimalField(max_digits=10, decimal_places=3)

class classes(models.Model):
    CourseID = models.ForeignKey(courses, on_delete = models.DO_NOTHING)
    Term = models.TextField()
    Year = models.DecimalField(max_digits=10, decimal_places=3)
    Instructor = models.TextField()
    Classroom = models.TextField()
    ClassTime = models.TextField()

class stuclasses(models.Model):
    ClassID = models.ForeignKey(classes, on_delete = models.CASCADE)
    StudentID = models.ForeignKey(students, on_delete = models.CASCADE)
    Grade = models.ForeignKey(GradeValues, on_delete = models.CASCADE)