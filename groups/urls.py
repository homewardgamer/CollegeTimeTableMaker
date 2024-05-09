from django.urls import path

from . import views

urlpatterns = [
    path('college/<randomid>/groups/', views.groupdisplay, name="groupview"),
    path('college/<randomid>/groups/add/', views.groupadd, name="addgroup"),
    path('college/<randomid>/groups/<groupslug>/edit/', views.groupedit, name="editgroup"),
    path('college/<randomid>/groups/<groupslug>/delete/', views.groupdelete, name="deletegroup"),
    path('college/<randomid>/groups/<groupslug>/', views.groupview, name="groupdisplay"),
    path('college/<randomid>/groups/<groupslug>/classes/', views.classview, name="classview"),
    path('college/<randomid>/groups/<groupslug>/classes/add/', views.classadd, name="addclass"),
    path('college/<randomid>/groups/<groupslug>/classes/<classslug>/edit/', views.classedit, name="editclass"),
    path('college/<randomid>/groups/<groupslug>/classes/<classslug>/delete/', views.classdelete, name="deleteclass"),
    path('college/<randomid>/groups/<groupslug>/breaks/', views.breakview, name="breakview"),
    path('college/<randomid>/groups/<groupslug>/breaks/add/', views.breakadd, name="addbreak"),
    path('college/<randomid>/groups/<groupslug>/breaks/<breakid>/edit/', views.breakedit, name="editbreak"),
    path('college/<randomid>/groups/<groupslug>/breaks/<breakid>/delete/', views.breakdelete, name="deletebreak"),
    path('college/<randomid>/groups/<groupslug>/routine/', views.routineview, name="routineview"),
    path('college/<randomid>/groups/<groupslug>/routine/add/', views.routineadd, name="addroutine"),
    path('college/<randomid>/groups/<groupslug>/routine/<routineid>/edit/', views.routineedit, name="editroutine"),
    path('college/<randomid>/groups/<groupslug>/routine/<routineid>/delete/', views.routinedelete, name="deleteroutine"),
    path('college/<randomid>/groups/<groupslug>/subjects/', views.groupsubjectsiew, name="groupsubjectsview"),
    path('college/<randomid>/groups/<groupslug>/subjects/add/', views.groupsubjectsadd, name="addgroupsubject"),
    path('college/<randomid>/groups/<groupslug>/subjects/<subjectslug>/edit/', views.groupsubjectsedit, name="editgroupsubject"),
    path('college/<randomid>/groups/<groupslug>/subjects/<subjectslug>/delete/', views.groupsubjectsdelete, name="deletegroupsubject"),
    path('college/<randomid>/groups/<groupslug>/specifications/', views.specificationsview, name="specificationsview"),
    path('college/<randomid>/groups/<groupslug>/specifications/add/', views.specificationsadd, name="addspecification"),
    path('college/<randomid>/groups/<groupslug>/specifications/<specificid>/edit/', views.specificationsedit, name="editspecification"),
    path('college/<randomid>/groups/<groupslug>/specifications/<specificid>/delete/', views.specificationsdelete, name="deletespecification"),
    path('college/<randomid>/groups/<groupslug>/lessons/', views.lessonsview, name="lessonsview"),
    path('college/<randomid>/groups/<groupslug>/lessons/add/', views.lessonsadd, name="addlesson"),
    path('college/<randomid>/groups/<groupslug>/lessons/<lessonid>/edit/', views.lessonsedit, name="editlesson"),
    path('college/<randomid>/groups/<groupslug>/lessons/<lessonid>/delete/', views.lessonsdelete, name="deletelesson"),
]