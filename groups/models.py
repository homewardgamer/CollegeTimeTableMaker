from django.db import models
from college.models import College, Subjects, Faculties, Streams
from django.utils.text import slugify
from django.conf import settings

# Store different groups by a college
class CollegeGroups(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    groupname = models.CharField(max_length=100)
    slug = models.SlugField()
    lessonduration = models.PositiveIntegerField()

    class Meta:
        verbose_name = ("Group")
        verbose_name_plural = ("Groups")

    def __str__(self):
        return f"{self.groupname} of the college {self.college.collegename}"

    # Slugify the groupname as you save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.groupname)
        super(CollegeGroups, self).save(*args, **kwargs)

# Store routine for a given group
class Grouproutine(models.Model):
    group = models.ForeignKey(CollegeGroups, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=settings.DAYS)
    starttime = models.TimeField()
    endtime = models.TimeField()

    class Meta:
        verbose_name = ("Group routine")
        verbose_name_plural = ("Group routines")

    def __str__(self):
        return f"{self.group.groupname} routine"

# Store breaks for a  given group
class Groupbreaks(models.Model):
    group = models.ForeignKey(CollegeGroups, on_delete=models.CASCADE)
    breakname = models.CharField(max_length=100)
    slug = models.SlugField()
    day = models.CharField(max_length=20, choices=settings.DAYS)
    starttime = models.TimeField()
    endtime = models.TimeField()

    class Meta:
        verbose_name = ("Group break")
        verbose_name_plural = ("Group breaks")

    def __str__(self):
        return f"{self.group.groupname} - {self.breakname}"

    # Slugify the breakname as you save
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.breakname} {self.starttime} {self.endtime}")
        super(Groupbreaks, self).save(*args, **kwargs)

# Store subjects in a given group
class Groupsubjects(models.Model):
    group = models.ForeignKey(CollegeGroups, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Group subject")
        verbose_name_plural = ("Group subjects")

    def __str__(self):
        return f"{self.subject.subjectname}"

# Store classes in a given group. Has a method to check if an object can be deleted.
class Groupclasses(models.Model):
    group = models.ForeignKey(CollegeGroups, on_delete=models.CASCADE)
    stream = models.ForeignKey(Streams, on_delete=models.CASCADE)
    #classfaculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    classname = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = ("Group class")
        verbose_name_plural = ("Group classes")

    def __str__(self):
        return f"{self.classname} - {self.stream.streamname}"

    # Slugify the classname as you save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.classname + self.stream.streamname)
        super(Groupclasses, self).save(*args, **kwargs)

    # Check if can delete this class
    def ifcandelete(self):
        from timetable.models import Timetablelessons, Timetablebreaks
        check1 = Timetablelessons.objects.filter(theclass__id=self.id).count()
        check2 = Timetablebreaks.objects.filter(theclass__id=self.id).count()

        # If there are timetable models using this class
        if (check1 > 0) or (check2 > 0):
            return False
        else:
            return True

# Store faculty, class and subject relating to a lesson plan for creation of a Timetable
class Groupsubjectfaculties(models.Model):
    groupsubjects = models.ForeignKey(Groupsubjects, on_delete=models.CASCADE)
    theclass = models.ForeignKey(Groupclasses, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    nooflessonsperweek = models.PositiveIntegerField()

    class Meta:
        verbose_name = ("Group subject faculty")
        verbose_name_plural = ("Group subject faculties")

    def __str__(self):
        return f"Subject: {self.groupsubjects.subject.subjectname} - Class: {self.theclass.classname} - Stream: {self.theclass.stream.streamname} Faculty: {self.faculty.facultyname}"

# Store specifications about a particular Group for tietable creation.
class GroupSpecifiction(models.Model):
    groupsubjectfaculties = models.ForeignKey(Groupsubjectfaculties, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=settings.DAYS)
    starttime = models.TimeField()
    endtime = models.TimeField()

    class Meta:
        verbose_name = ("Group specificationr")
        verbose_name_plural = ("Group specificationrs")

    def __str__(self):
        return f"{self.groupsubjectfaculties.groupsubjects.group.groupname} Specifications"
