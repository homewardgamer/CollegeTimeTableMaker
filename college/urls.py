from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="index"),
    path('account/<randomid>/delete', views.deleteaccount, name="deleteaccount"),
    path('account/edit/', views.editaccount, name="editaccount"),
    path('account/changepassword/', views.changepassword, name="changepassword"),
    path('account/', views.useraccount, name="useraccount"),
    path('colleges/', views.collegedisplay, name="collegedisplay"),
    path('college/add/', views.addcollege, name="addcollege"),
    path('college/<randomid>/edit/', views.editcollege, name="editcollege"),
    path('college/<randomid>/delete/', views.deletecollege, name="deletecollege"),
    path('college/<randomid>/', views.collegeview, name="collegeview"),
    path('college/<randomid>/stream/', views.streamsview, name="streamview"),
    path('college/<randomid>/stream/add/', views.streamsadd, name="addstream"),
    path('college/<randomid>/stream/<streamslug>/edit/', views.streamsedit, name="editstream"),
    path('college/<randomid>/stream/<streamslug>/delete/', views.streamsdelete, name="deletestreams"),
    path('college/<randomid>/faculty/', views.facultiesview, name="facultyview"),
    path('college/<randomid>/faculty/add/', views.facultyadd, name="addfaculty"),
    path('college/<randomid>/faculty/<facultyrandomid>/edit/', views.facultyedit, name="editfaculty"),
    path('college/<randomid>/faculty/<facultyrandomid>/delete/', views.facultydelete, name="deletefaculties"),
    path('college/<randomid>/subject/', views.subjectsview, name="subjectview"),
    path('college/<randomid>/subject/add/', views.subjectsadd, name="addsubject"),
    path('college/<randomid>/subject/<subjectslug>/edit/', views.subjectsedit, name="editsubject"),
    path('college/<randomid>/subject/<subjectslug>/delete/', views.subjectsdelete, name="deletesubject"),
]