from statistics import mode
from turtle import color
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.utils.text import slugify
from colorfield.fields import ColorField
from .validators import validate_logo

# Store info on registred users
class User(AbstractUser):
    randomid = models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return f"{self.username}"


# Store info on colleges by a particular users
class College(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    collegename = models.CharField(max_length=200)
    randomid = models.CharField(max_length=60, unique=True)
    collegelogo = models.ImageField(upload_to='logo', validators=[validate_logo], default='logo.png')
        
    class Meta:
        verbose_name = ("College")
        verbose_name_plural = ("Colleges")

    def __str__(self):
        return f"{self.collegename} by {self.user.id}"

# Store info on subjects by a given college Has a method to check if an object can be deleted.
class Subjects(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    subjectname = models.CharField(max_length=100)
    slug = models.SlugField()
    color = ColorField()

    class Meta:
        verbose_name = ("Subject")
        verbose_name_plural = ("Subjects")

    def __str__(self):
        return f"{self.subjectname}"

    # Slugify the subjectname as you save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subjectname)
        super(Subjects, self).save(*args, **kwargs)

    # Check if can delete this subject
    def ifcandelete(self):
        from timetable.models import Timetablelessons
        check1 = Timetablelessons.objects.filter(subject__id=self.id).count()

        # If there are timetable models using this subject
        if (check1 > 0):
            return False
        else:
            return True

# Store info on faculties by a given . Has a method to check if an object can be deleted.
class Faculties(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    facultyname = models.CharField(max_length=100)
    randomid = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = ("Faculty")
        verbose_name_plural = ("Faculties")

    def __str__(self):
        return f"{self.facultyname}"

    # Check if can delete this faculty
    def ifcandelete(self):
        from timetable.models import Timetablelessons
        check1 = Timetablelessons.objects.filter(faculty__id=self.id).count()

        # If there are timetable models using this faculty
        if (check1 > 0):
            return False
        else:
            return True

# Store info on routine by a given faculty.
class FacultiesRoutine(models.Model):
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=settings.DAYS)
    starttime = models.TimeField()
    endtime = models.TimeField()

    class Meta:
        verbose_name = ("Faculty Routine")
        verbose_name_plural = ("Faculty Routines")

    def __str__(self):
        return f"{self.faculty.facultyname} Routine on {self.day}"

# Store info on streams by a given college. Has a method to check if an object can be deleted.
class Streams(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    streamname = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = ("Stream")
        verbose_name_plural = ("Streams")

    def __str__(self):
        return f"{self.streamname}"

    # Slugify the streamname as you save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.streamname)
        super(Streams, self).save(*args, **kwargs)

    # Check if can delete this stream
    def ifcandelete(self):
        from timetable.models import Timetablelessons, Timetablebreaks
        check1 = Timetablelessons.objects.filter(theclass__stream__id=self.id).count()
        check2 = Timetablebreaks.objects.filter(theclass__stream__id=self.id).count()

        # If there are timetable models using this stream
        if (check1 > 0) or (check2 > 0):
            return False
        else:
            return True