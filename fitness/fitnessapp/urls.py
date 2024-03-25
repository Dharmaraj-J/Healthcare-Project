from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),

    path('loginpage/',views.loginpage,name="loginpage"),
    path('approval',views.approval,name='approval'),

    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'), 

    path('mainpage',views.mainpage,name='mainpage'), 

    path('handlelogout/',views.handlelogout, name='handlelogout'),  

    path('cycling',views.cycling, name='cycling'),  
    path('running',views.running, name='running'),
    path('swimming',views.swimming, name='swimming'), 
    path('gym',views.gym, name='gym'),     

    path('leaderboard_view',views.leaderboard_view, name='leaderboard_view'),
    path('update_leaderboard',views.update_leaderboard, name='update_leaderboard'),  

    path('set_goal', views.set_goal, name='set_goal'),
    path('generate_report', views.generate_report, name='generate_report'),
    
    path('record_workout', views.record_workout, name='record_workout'),

    path('userview', views.userview, name='userview'),

    path('editprofile/<int:pk>', views.editprofile, name='editprofile'),
  
    
    # path('leaderboard', views.leaderboard, name='leaderboard'),
]
