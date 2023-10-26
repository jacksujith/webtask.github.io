from stockapp import views
from .views import UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.homepage,name='mainpage'),
    path('explore',views.explore,name='explore'),
    path('activity',views.activity,name='activity'),
    path('leaderboard',views.leaderboard,name='leaderboard'),
    path('payouts',views.payouts,name='payouts'),
    path('contact/',views.contact,name='contactus'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('forgot/',views.forgot,name='forgot'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard1',views.dashboard1,name='dashboard1'),
    # path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
    #      name="validate-username"),
    path('token',views.token,name='token'),
    path('success',views.success,name='success'),
    path('accounts/',views.accounts,name='accounts'),
    path('billing/',views.billing,name="billing"),
    path('utilities/',views.utilities,name="utilities"),
    path('calender/',views.calender,name='calender'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('comptition',views.comptition,name='comptition'),
    path('help',views.help,name='help'),
    path('payment',views.Payment,name='payment'),
    path('activate',views.activate,name='activate'),
    path('inactivate',views.inactivate,name='inactivate'),
    path('branched',views.branched,name='branched'),

    
]
