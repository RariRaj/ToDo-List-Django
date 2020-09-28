from django.urls import path,include
from home import views


urlpatterns = [
    
    path('',views.index,name="index"),
    path('task',views.task,name="task"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('cross_off/<str:id>',views.cross_off,name="cross_off"),
    path('uncross/<str:id>',views.uncross,name="uncross"),
    path('update/<str:id>',views.update,name="update"),
    path('test',views.test,name="test")
]
