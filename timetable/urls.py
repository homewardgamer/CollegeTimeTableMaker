from django.urls import path

from . import views

urlpatterns = [
    path('college/<randomid>/timetable/', views.timetablesview, name="timetablesview"),
    path('college/<randomid>/timetable/<timetableid>/edit/', views.edittimetable, name="edittimetable"),
    path('college/<randomid>/timetable/<timetableid>/delete/', views.deletetimetable, name="deletetimetable"),
    path('college/<randomid>/timetable/<timetableid>/', views.timetablesingroup, name="timetablesingroup"),
    path('college/<randomid>/checktimetable/', views.timetablecheck, name="timetablecheck"),
    path('college/<randomid>/generatetimetable/', views.generatetimetable, name="generatetimetable"),
    path('college/<randomid>/timetable/<timetableid>/view/<classlug>/', views.onetimetable, name="onetimetable"),
    path('college/<randomid>/timetable/<timetableid>/view/<classlug>/pdf/', views.pdftimetable, name="pdftimetable"),
]