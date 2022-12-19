from django.urls import path
from . import views
from .views import StandardDetail,SubjectDetail,AddSubject, AddStandard,UpdateStandard, Deletestandard,UpdateSubject,DeleteSubject,get_faculty
app_name = 'school'

urlpatterns = [
    path('', StandardDetail.as_view(), name='example1'),
    path('<pk>/update', UpdateStandard.as_view(), name='example'),
    path('<pk>/delete', Deletestandard.as_view()),
    # path('subject', views.subject_details),
    path('subject',SubjectDetail.as_view()),
    path('subject/<pk>/update', UpdateSubject.as_view()),
    path('subject/<pk>/delete', DeleteSubject.as_view()),
    path('addsubject', AddSubject.as_view()),
    path('addstandard', AddStandard.as_view()),
    path('login', views.Input1),
    path('base', views.get_faculty),

]