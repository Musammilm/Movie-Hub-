from django.urls import path
from app import views

urlpatterns=[
    path('',views.index),
    path('home',views.home),
    path('about',views.about),
    path('userlogin',views.userlogin),
    path('userlogged<str:tk>',views.userlogged,name="userlogged"),
    path('moviedetails <str:tk>',views.moviedetails,name='teach'),
    path('booking <str:pk>',views.booking,name="book"),
    path('bookedsuccess',views.bookedsuccess),
    # path('setshow',views.setshow,name='set'),
    path('theatrelogged',views.theatrelogged),
    path('addmovie',views.addmovie),
    path('succes',views.succes),
    path('theatrelogin',views.theatrelogin),
    path('theatreregister',views.theatreregister),
    path('userregister/',views.userregister),
    path('user_main',views.user_main,name="user_main"),
    path('booking_details',views.booking_details),
    path('tc_balance',views.tc_balance),
    
    path('adminlogin',views.adminlogin),
    path('adminlogged',views.adminlogged),
    path('admin_theatre',views.admin_theatre),
    path('recommend',views.recommend,name="recommend"),
    path('similarity',views.similarity,name="similarity"),
    path('user_activate<str:ttk>',views.user_activate,name="user_activate"),
    path('admin_1theatre<str:cck>',views.admin_1theatre,name="admin_1theatre"),
    path('delete_theatre<str:cck>',views.delete_theatre,name="delete_theatre"),

    path('tfeedback',views.tfeedback),
    path('admin_feedback',views.admin_feedback),
    path('ufeedback',views.ufeedback),
    path('payment',views.payment),
    path('tickets',views.tickets),
    path('delticket<str:bk>',views.delticket,name="delticket"),
    path('paymentSS',views.paymentSS),
    

]

