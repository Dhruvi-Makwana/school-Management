from django.urls import path
from . import views
from .views import UserDetail, Detail,AddUser
app_name = 'user'

urlpatterns = [
    # path('', views.index), #name='index'),
    path('', UserDetail.as_view()),
    path('<int:pk>/',Detail.as_view()),  #name='detail'),
    path('adduser/', AddUser.as_view(), name='adduser'),
    # path('', View1.as_view()),
    # path('<pk>', View2.as_view()),
    # path('<pk>/update', View3.as_view())
    # path('<pk>/delete',View4.as_view())
]


#
# from .views import View1,View2
# urlpatterns = [
#     path('', View1.as_view()),
#     path('<pk>',View2.as_view()),
# ]
# def test(id = None):
#     return id;
#
# print(test())
